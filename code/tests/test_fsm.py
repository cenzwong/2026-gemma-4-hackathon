import pytest
from unittest.mock import MagicMock, patch
from FSM.engine import MedicalAgentFSM, State

@pytest.fixture
def mock_b():
    with patch('FSM.engine.b') as mock_b_client:
        yield mock_b_client

@pytest.fixture
def mock_kiwix():
    with patch('FSM.engine.Kiwix') as mock_kiwix_client:
        yield mock_kiwix_client

@pytest.fixture
def mock_stream():
    with patch('FSM.engine.stream_generate_content') as mock_stream_gen:
        yield mock_stream_gen

def test_fsm_initial_state():
    fsm = MedicalAgentFSM()
    assert fsm.state == State.IDLE
    assert fsm.context['history'] == []

def test_triage_insufficient_info(mock_b):
    fsm = MedicalAgentFSM()
    
    # Mock EvaluateInformation to return insufficient info
    eval_mock = MagicMock()
    eval_mock.has_enough_info = False
    mock_b.EvaluateInformation.return_value = eval_mock
    
    # Mock ExtractSymptoms
    symp_mock = MagicMock()
    symp_mock.symptoms = ["headache"]
    mock_b.ExtractSymptoms.return_value = symp_mock
    
    # Mock FollowUpQuestion
    mock_b.AskFollowUpQuestion.return_value = "How long have you had the headache?"
    
    fsm.run("I have a headache")
    
    assert fsm.state == State.IDLE
    assert "User: I have a headache" in fsm.context['history'][0]
    assert "Agent: How long have you had the headache?" in fsm.context['history'][1]
    mock_b.EvaluateInformation.assert_called_once()
    mock_b.ExtractSymptoms.assert_called_once()
    mock_b.AskFollowUpQuestion.assert_called_once()

def test_triage_sufficient_info_and_search(mock_b, mock_kiwix, mock_stream):
    fsm = MedicalAgentFSM()
    
    # Mock EvaluateInformation to return sufficient info
    eval_mock = MagicMock()
    eval_mock.has_enough_info = True
    mock_b.EvaluateInformation.return_value = eval_mock
    
    # Mock DecodeQuestion
    mock_b.DecodeQuestion.return_value = ["chest pain"]
    
    # Mock Kiwix Books
    mock_book = MagicMock()
    mock_book.name = "wiki_medicine"
    
    mock_article = MagicMock()
    mock_article.title = "Angina"
    mock_article.url = "/angina"
    mock_article.snippet = "Chest pain snippet"
    mock_article.path = True
    
    mock_header = MagicMock()
    mock_header.name = "Symptoms"
    mock_header.text = "Pain in the chest"
    mock_article.get_article.return_value = ("<html></html>", [mock_header])
    
    mock_book.search_article.return_value = [mock_article]
    mock_kiwix.return_value.get_kiwix_book.return_value = [mock_book]
    
    # Mock stream generation
    mock_stream.return_value = ["This is a ", "mocked response."]
    
    fsm.run("I have crushing chest pain")
    
    assert fsm.state == State.IDLE
    # verify kiwix context is set correctly
    assert len(fsm.context['kiwix_full_texts']) == 1
    assert "Title: Angina" in fsm.context['kiwix_full_texts'][0]
    assert "Symptoms: Pain in the chest" in fsm.context['kiwix_full_texts'][0]
    
    # Verify response generated
    assert "Agent: This is a mocked response." in fsm.context['history'][-1]

def test_search_kiwix_fallback(mock_b, mock_kiwix, mock_stream):
    fsm = MedicalAgentFSM()
    
    eval_mock = MagicMock()
    eval_mock.has_enough_info = True
    mock_b.EvaluateInformation.return_value = eval_mock
    
    # Multiple keywords for fallback testing
    mock_b.DecodeQuestion.return_value = ["very specific bad query", "fever"]
    
    mock_book = MagicMock()
    mock_book.name = "wiki_medicine"
    
    mock_article = MagicMock()
    mock_article.title = "Fever"
    mock_article.url = "/fever"
    mock_article.snippet = "Fever snippet"
    mock_article.path = True
    mock_header = MagicMock()
    mock_header.name = "Overview"
    mock_header.text = "High temp"
    mock_article.get_article.return_value = ("<html></html>", [mock_header])
    
    # search_article returns [] for the first query, and [mock_article] for the second
    def mock_search(query):
        if query == "very specific bad query":
            return []
        return [mock_article]
    
    mock_book.search_article.side_effect = mock_search
    mock_kiwix.return_value.get_kiwix_book.return_value = [mock_book]
    
    mock_stream.return_value = ["Result"]
    
    fsm.run("I have a fever")
    
    assert fsm.state == State.IDLE
    assert len(fsm.context['kiwix_full_texts']) == 1
    assert "Title: Fever" in fsm.context['kiwix_full_texts'][0]

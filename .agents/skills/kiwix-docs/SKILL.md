---
name: kiwix-docs
description: The original kiwix-docs for reference.
---

================================================
FILE: README.md
================================================
Kiwix tools
===========

The Kiwix tools is a collection of [Kiwix](https://kiwix.org) related
command line tools:
* kiwix-manage: Manage XML based library of ZIM files
* kiwix-search: Full text search in ZIM files
* kiwix-serve: HTTP daemon serving ZIM files

[![latest release](https://img.shields.io/github/v/tag/kiwix/kiwix-tools?label=latest%20release&sort=semver)](https://download.kiwix.org/release/kiwix-tools/)
[![Repositories](https://img.shields.io/repology/repositories/kiwix-tools?label=repositories)](https://github.com/kiwix/kiwix-tools/wiki/Repology)
[![Docker](https://ghcr-badge.egpl.dev/kiwix/kiwix-tools/latest_tag?label=docker)](https://ghcr.io/kiwix/kiwix-tools)
[![Docker](https://ghcr-badge.egpl.dev/kiwix/kiwix-tools/latest_tag?label=docker%20(kiwix-serve))](https://ghcr.io/kiwix/kiwix-tools)
[![Build Status](https://github.com/kiwix/kiwix-tools/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/kiwix/kiwix-tools/actions/workflows/ci.yml?query=branch%3Amain)
[![Doc](https://readthedocs.org/projects/kiwix-tools/badge/?style=flat)](https://kiwix-tools.readthedocs.org/en/latest/?badge=latest)
[![CodeFactor](https://www.codefactor.io/repository/github/kiwix/kiwix-tools/badge)](https://www.codefactor.io/repository/github/kiwix/kiwix-tools)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

Disclaimer
----------

This document assumes you have a little knowledge about software
compilation. If you experience difficulties with the dependencies or
with the Kiwix tools compilation itself, we recommend to have a look
to [kiwix-build](https://github.com/kiwix/kiwix-build).

Preamble
--------

Although the Kiwix tools can be compiled/cross-compiled on/for many
systems, the following documentation explains how to do it on POSIX
ones. It is primarily thought for GNU/Linux systems and has been tested
on recent releases of
[Debian](https://debian.org)/[Ubuntu](https://ubuntu.com) and
[Fedora](https://getfedora.org).

Dependencies
------------

The Kiwix tools rely on a few third party software libraries. They are
prerequisites to the Kiwix tools compilation. Therefore, following
libraries need to be available:
* [libkiwix](https://github.com/kiwix/libkiwix) (package `libkiwix` on Debian/Ubuntu)
* [libzim](https://github.com/openzim/libzim) (package `libzim` on Debian/Ubuntu)

These dependencies may or may not be packaged by your operating
system. They may also be packaged but only in an older version. They
may be also packaged but without providing a static version. The
compilation script will tell you if one of them is missing or too old.
In the worse case, you will have to download and compile bleeding edge
version by hand.

If you want to install these dependencies locally, then use the
kiwix-tools directory as install prefix.

If you want to compile Kiwix tools statically, the dependencies should
be compiled statically (provide a `lib...a` library), for example by
using `--enable-static` with `./configure`.

Environment
-------------

The Kiwix tools build using [Meson](http://mesonbuild.com/) version
0.43 or higher. Meson relies itself on Ninja, pkg-config and a few other
compilation tools. Install them first:
* [Meson](http://mesonbuild.com/)
* [Ninja](https://ninja-build.org/)
* [pkg-config](https://www.freedesktop.org/wiki/Software/pkg-config/)

These tools should be packaged if you use a cutting edge operating
system. If not, have a look to the [Troubleshooting](#Troubleshooting)
section.

Compilation
-----------

Once all dependencies are installed, you can compile Kiwix tools with:
```bash
meson . build
ninja -C build
```

By default, it will compile dynamic linked libraries. If you want
statically linked libraries, you can add `-Dstatic-linkage=true`
option to the Meson command.

Depending of you system, `ninja` may be called `ninja-build`.

Installation
------------

If you want to install the Kiwix tools, here we go:
```bash
ninja -C build install
```

You might need to run the command as `root` (or using `sudo`),
depending on where you want to install the Kiwix tools. After the
installation succeeded, you may need to run ldconfig (as `root`).

Uninstallation
------------

If you want to uninstall the Kiwix tools:
```bash
ninja -C build uninstall
```

Like for the installation, you might need to run the command as `root`
(or using `sudo`).

Docker
------

An official Docker image of the Kiwix tools can be found on 
[GHCR](https://ghcr.io/kiwix/kiwix-tools). A
`kiwix-serve` dedicated Docker image [exists
too](https://ghcr.io/kiwix/kiwix-serve).

Troubleshooting
---------------

If you need to install Meson "manually":
```bash
virtualenv -p python3 ./ # Create virtualenv
source bin/activate      # Activate the virtualenv
pip3 install meson       # Install Meson
hash -r                  # Refresh bash paths
```

If you need to install Ninja "manually":
```bash
git clone git://github.com/ninja-build/ninja.git
cd ninja
git checkout release
./configure.py --bootstrap
mkdir ../bin
cp ninja ../bin
cd ..
```

If the compilation still fails, you might need to get a more recent
version of a dependency than the one packaged by your Linux
distribution. Try then with a source tarball distributed by the
problematic upstream project or even directly from the source code
repository.

License
-------

[GPLv3](https://www.gnu.org/licenses/gpl-3.0) or later, see
[COPYING](COPYING) for more details.



================================================
FILE: AUTHORS
================================================
Emmanuel Engelhart <kelson@kiwix.org>
Renaud Gaudin <reg@kiwix.org>
Christian Pühringer <cip@gmx.at>
Fabien Coullon <fcoulon@linterweb.com>
Guillaume Duhamel <gduhamel@linterweb.com>
Wilfredo Rodriguez <wilfredor@kiwix.org>
Jorge Gonzalez <jag2kn@gmail.com>
Richzendy <richzendy@fedoraproject.org>
Ayoub Dardory <ayoubuto@gmail.com>
Rashiq Ahmad <rashiq.z@gmail.com>
Isaac Hutt <mhutti1@gmail.com>
Elad Keyshawn <elad.keyshawn@gmail.com>
Matthieu Gautier <mgautier@kymeria.fr>
Translatewiki comunity https://translatewiki.net/wiki/Translating:Kiwix



================================================
FILE: Changelog
================================================
kiwix-tools 3.8.2
=================

 * Other
   - Fix PPA publishing (@kelson42 #800)
   - Use windows-2025 CI runner (@kelson42 #805)
   - Updated documentation of lang and category filters in catalog query API endpoints (@veloman-yunkan #804)

kiwix-tools 3.8.1
=================

 * Kiwix server
   - Hide port number in URL when server is running on port 80 (@vighnesh-sawant #763)
   - Better deal with container /data dir permissions (@kelson42 #787)

 * Other
   - Fix kiwix-manage docopt integration (@kelson42 #783)

kiwix-tools 3.8.0
=================

 * Kiwix server
   - Improve message when server is running on standard port (@vighnesh-sawant #763)
   - Update container base image to latest Alpline version (@yashgoyal0110 #771)
   - Container image to use unprivileged user (@Sedetisu #755)
   - Empty urlRootLocation doesn't disable book preview links anymore (@veloman-yunkan #1224)
   - Add support of IPv6 (@sgourdas #673 #704)
   - Popups are allowed to escape the browser sandbox (@veloman-yunkan #1208)

 * Other
   - Stop publishing on Ubuntu 20.04 PPA (@kelson42 #748)
   - Use Docopt for command line argument parsing (@mgautierfr #695)

 * Compilation & Packaging
   - Based on libkiwix 14.1.0 (@kelson42 #773)
   - Improve CI/CD (@kelson42 #681 #698 #702 #705 #720 #722, @mgautierfr #695)

kiwix-tools 3.7.0
=================

 * Fixed ZIM name vs Book name confusion in documentation (@veloman-yunkan #663)
 * Fixes compilation dependencies to rely on appropriate version (@kelson42 #667)
 * New --skipInvalid Kiwix Server command line option (@schuellerf @kelson42 #666)

kiwix-tools 3.6.0
=================

 * Improved kiwix-serve man page (@iArchitSharma #626)
 * C++17 compliant code base (@mgautierfr #636)
 * Support of libkiwix13 (@mgautierfr #633)
 * Additional docker images archs for armv6 and i386 (@rgaudin #622)

kiwix-tools 3.5.0
=================

 * Do not use `--static` option when compiling on MacOs (@mgautierfr #615)
 * Move main branch from `master` to `main`.
 * Fix docker image (@jacroe #597)
 * Various CI improvements (@kelson42)

kiwix-serve
-----------

 * Add documentation about the kiwix-serve API (@veloman-yunkan #586)
   https://kiwix-tools.readthedocs.io/en/latest/kiwix-serve.html#http-api

kiwix-tools 3.4.0
=================

 * Remove last reference to kiwix-read tool (@legoktm #569)

kiwix-serve
-----------

 * Fix broken indentation in usage (@kelson42 #560)
 * Exit if wrong arguments are passed (@kelson42 #567)
 * Do not allow multiple values for same option (@juuz0 #564)
 * Fix default location of "rootLocation" (@rgaudin #571)
 * [DOCKER] Change default port to 8080 (@neyder #581)
 * [DOCKER] Simplify dockerfile (@rgaudin #582)

kiwix-manage
------------

 * Fix man page (@kelson42 #576)

kiwix-tools 3.3.0
=================

 * Remove kiwix-read tool (@veloman-yunkan #535)

kiwix-serve
-----------

 * Add an option to limit the number of connections for a same IP (@juuz0 #534)
 * Add an option to limit the number of zim in a multizim fulltext search (@mgautierfr #558)

kiwix-search
------------

 * Remove usage of libkiwix's deprecated api (@veloman-yunkan #535)

kiwix-manage
------------

 * Correctly return a value !0 if something went wrong (@mgautierfr #553)


kiwix-tools 3.2.0
=================

 * Print the version of all dependencies (@kelson42 #516)
 * Better Docker images (@kelson42 @rgaudin)
 * Update Readme (@kelson42)
 * Build debian packages on CI (@legoktm #394)
 * Add man pages for kiwix-read and kiwix-search (@legoktm #392)
 * Various fixes (@legoktm @hashworks @mgautierfr)


kiwix-serve
-----------

 * Print the url on which a user can connect to on startup (@juuz0 #499 #522)
 * Reload library on SIGHUP signal (@veloman-yunkan #497)
 * Add a option `--monitorLibrary` to monitor and automically reload the library
   (@veloman-yunkan #503)
 * Correct handling of SIGTERM and SIGINT (@veloman-yunkan #488)
 * Add `--customIndexTemplate` option (@manan #477)
 * Add `--help` option (@kelson42 #511)


kiwix-tools 3.1.2
=================

 * Use new threadsafe API of kiwix-lib to do suggestions search.

kiwix-tools 3.1.1
=================

 * Fix compilation on Windows' CI

kiwix-tools 3.1.0
=================

 * [SERVER] Add option to block external links

kiwix-tools 3.0.3
=================

 * [MANAGER] Fix broken --version argument parsing

kiwix-tools 3.0.2
=================

 * New option --version for all tools
 * Remove benchmark.sh file.
 * [DOCKER] Add ability to download a file at container start.
 * [CI] Move to github actions instead of travis.
 * [SERVER] Trust the given library by default.
 * [SERVER] Add shortcut alias for option `--address` and `--nodatealias`

kiwix-tools 3.0.1
=================

 * Fix --nodatealiases inverted logic regression

kiwix-tools 3.0.0
=================

 * Move kiwix-serve implementation in kiwix-lib.

kiwix-tools 2.1.0
=================

 * Fix few compilation errors.

kiwix-serve
-----------

 * Use new api to filter the library.
 * Mobile friendly top bar.
 * Add notag parameter to be able to exclude tags from the zim search.


kiwix-tools 2.0.0
=================

kiwix-manage
-----------

 * Better usage()
 * Adding multiple files bug fix
 * Remove download command.

kiwix-serve
-----------

 * Better usage()
 * Display properly welcome page on 3 columns
 * New welcome page footer "Powered by Kiwix"

kiwix-tools 1.2.1
=================

kiwix-serve
-----------

 * Always use POLL when avaible.

kiwix-tools 1.2.0
=================

 * Remove rpath for installed binaries.

kiwix-serve
-----------

 * New Dockerfile of kiwix-serve
 * New --nodatealiases option
 * Do not use POLL on windows

kiwix-manage
------------

 * Do not show all books if book ids has been provided.
 * Be able to add several zim files in the same time in a library.

kiwix-tools 1.1.0
=================

kiwix-serve
-----------

 * Fix bug about handling of absolute url in old zim file.
 * All the catalog to be searched by tags.

kiwix-tools 1.0.0
=================

 * [CI] Use the new deps archive xz
 * Move version 1.0.0. There is no need to stay in pre 1.0 version.

kiwix-serve
-----------

 * Correctly implement redirection.
   kiwix-serve now return a 302 http status code instead of resolving the
   redirection internally and return the content.


kiwix-tools 0.9.0
=================

 * Update README
 * Update man pages
 * Remove support of external indexes (manage, search, serve)
 * Update build system as we don't use ctpp2 anymore
 * Update to last kiwix-lib API.

kiwix-manage
------------

 * Update usage.


kiwix-tools 0.8.0
=================

kiwix-manage
------------

 * Be able to remove several books from the library in one command.

kiwix-tools 0.7.0
=================

 * Adapt to kiwix-lib new API

kiwix-serve
-----------

 * Dumps only valid books in the opdsfeed.
 * Allow the opds feed to be filtered by lang and paginated.

kiwix-manage
------------

 * Add a download command to download a remote book locally
 * Book are referenced by bookId not index.
 * No more indexType option as it is always XAPIAN.

kiwix-tools 0.6.1
=================

kiwix-serve
-----------

 * Update README.
 * Fix crash when `--library` flag is provided without value.
 * Correctly handle mimetype of file without extension on 64bits.
 * Minor fixes

kiwix-tools 0.6.0
=================

 * remove kiwix-install tool.

kiwix-serve
-----------

 * Improved taskbar #160
 * Fix global page when using the option `--nosearchbar`
 * Return 404 for missing resources
 * Fix compilation for gcc 4.8.

kiwix-manage
------------

 * Returns proper exit code (not always 0)


kiwix-tools 0.5.0
=================

 * Build kiwix-tools setting the RPATH
 * Compile without warning.


kiwix-serve
------------

 * Serve metadata information using the "/meta" url.
 * Serve an OPDS stream of all zim handled by kiwix-serve
   All informations cannot be infer from the zim file itself,
   you should use a library.xml to provide needed information (url, ...)
 * Update kiwix-serve to use the new API of kiwix-lib

kiwix-tools 0.4.0
=================

 * Use gcc-5 on travis.

kiwix-serve
-----------

 * Accept zim file with `&` in the name
 * Do not cache (on client side) global search (as it can depends on the zim
   files handled)
 * Fix HTTP byte range handling. (#91)
 * Fix opening of relative path (#70)
 * Add a small (and hidden) API to do geo search.
 * Better request parsing. (#91)
 * Better handling of invalid request (#116)
 * Various bug fixes (#146, #150, #153, #165, #168, #165)

kiwix-search
------------

 * Add an option `--suggestion` to do suggestion search with
   kiwix-search.(#132)

kiwix-tools 0.3.0
=================

 * Move to C++11

kiwix-serve
-----------

 * Add a global taskbar in the welcome page to search in all zims (#49)
 * Serve the taskbar as css file instead of including it in the html (#68):
   * Better client caching
   * The html encoding is now in the first 1024 bytes and firefox correctly
     detect the encoding
 * Make kiwix-server multi-threaded (#82)
 * Correctly return 404 instead of crashing when request inexistant skin file
   (#83)
 * Correctly respond to bytes-range requests.(#84)
 * Directly respond to first request for a url instead of refusing the first
   connexion
 * Add support to relative url location. (#86)
 * Remove caching (on client side) for the welcome page. (#86)


kiwix-tools 0.2.0
=================

 * Remove indexer tools

kiwix-serve
-----------

 * Correctly fix the deflate data we send over http. (#15)
 * Update in the taskbar (or topbar):
    * Taskbar is responsive (github.com/kiwix/kiwix/issues/336)
    * Force css rules for the taskbar (and not be impacted by content's css)
 * Add `--nolibrarybutton` to hide the library button from the taskbar.
 * Rewrite of the welcome page.


kiwix-installer
---------------

 * Remove indexing functionnality



================================================
FILE: COPYING
================================================

		    GNU GENERAL PUBLIC LICENSE
		       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

			    Preamble

  The GNU General Public License is a free, copyleft license for
software and other kinds of works.

  The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
the GNU General Public License is intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.  We, the Free Software Foundation, use the
GNU General Public License for most of our software; it applies also to
any other work released this way by its authors.  You can apply it to
your programs, too.

  When we speak of free software, we are referring to freedom, not
price.  Our General Public Licenses are designed to make sure that you
have the freedom to distribute copies of free software (and charge for
them if you wish), that you receive source code or can get it if you
want it, that you can change the software or use pieces of it in new
free programs, and that you know you can do these things.

  To protect your rights, we need to prevent others from denying you
these rights or asking you to surrender the rights.  Therefore, you have
certain responsibilities if you distribute copies of the software, or if
you modify it: responsibilities to respect the freedom of others.

  For example, if you distribute copies of such a program, whether
gratis or for a fee, you must pass on to the recipients the same
freedoms that you received.  You must make sure that they, too, receive
or can get the source code.  And you must show them these terms so they
know their rights.

  Developers that use the GNU GPL protect your rights with two steps:
(1) assert copyright on the software, and (2) offer you this License
giving you legal permission to copy, distribute and/or modify it.

  For the developers' and authors' protection, the GPL clearly explains
that there is no warranty for this free software.  For both users' and
authors' sake, the GPL requires that modified versions be marked as
changed, so that their problems will not be attributed erroneously to
authors of previous versions.

  Some devices are designed to deny users access to install or run
modified versions of the software inside them, although the manufacturer
can do so.  This is fundamentally incompatible with the aim of
protecting users' freedom to change the software.  The systematic
pattern of such abuse occurs in the area of products for individuals to
use, which is precisely where it is most unacceptable.  Therefore, we
have designed this version of the GPL to prohibit the practice for those
products.  If such problems arise substantially in other domains, we
stand ready to extend this provision to those domains in future versions
of the GPL, as needed to protect the freedom of users.

  Finally, every program is threatened constantly by software patents.
States should not allow patents to restrict development and use of
software on general-purpose computers, but in those that do, we wish to
avoid the special danger that patents applied to a free program could
make it effectively proprietary.  To prevent this, the GPL assures that
patents cannot be used to render the program non-free.

  The precise terms and conditions for copying, distribution and
modification follow.

		       TERMS AND CONDITIONS

  0. Definitions.

  "This License" refers to version 3 of the GNU General Public License.

  "Copyright" also means copyright-like laws that apply to other kinds of
works, such as semiconductor masks.
 
  "The Program" refers to any copyrightable work licensed under this
License.  Each licensee is addressed as "you".  "Licensees" and
"recipients" may be individuals or organizations.

  To "modify" a work means to copy from or adapt all or part of the work
in a fashion requiring copyright permission, other than the making of an
exact copy.  The resulting work is called a "modified version" of the
earlier work or a work "based on" the earlier work.

  A "covered work" means either the unmodified Program or a work based
on the Program.

  To "propagate" a work means to do anything with it that, without
permission, would make you directly or secondarily liable for
infringement under applicable copyright law, except executing it on a
computer or modifying a private copy.  Propagation includes copying,
distribution (with or without modification), making available to the
public, and in some countries other activities as well.

  To "convey" a work means any kind of propagation that enables other
parties to make or receive copies.  Mere interaction with a user through
a computer network, with no transfer of a copy, is not conveying.

  An interactive user interface displays "Appropriate Legal Notices"
to the extent that it includes a convenient and prominently visible
feature that (1) displays an appropriate copyright notice, and (2)
tells the user that there is no warranty for the work (except to the
extent that warranties are provided), that licensees may convey the
work under this License, and how to view a copy of this License.  If
the interface presents a list of user commands or options, such as a
menu, a prominent item in the list meets this criterion.

  1. Source Code.

  The "source code" for a work means the preferred form of the work
for making modifications to it.  "Object code" means any non-source
form of a work.

  A "Standard Interface" means an interface that either is an official
standard defined by a recognized standards body, or, in the case of
interfaces specified for a particular programming language, one that
is widely used among developers working in that language.

  The "System Libraries" of an executable work include anything, other
than the work as a whole, that (a) is included in the normal form of
packaging a Major Component, but which is not part of that Major
Component, and (b) serves only to enable use of the work with that
Major Component, or to implement a Standard Interface for which an
implementation is available to the public in source code form.  A
"Major Component", in this context, means a major essential component
(kernel, window system, and so on) of the specific operating system
(if any) on which the executable work runs, or a compiler used to
produce the work, or an object code interpreter used to run it.

  The "Corresponding Source" for a work in object code form means all
the source code needed to generate, install, and (for an executable
work) run the object code and to modify the work, including scripts to
control those activities.  However, it does not include the work's
System Libraries, or general-purpose tools or generally available free
programs which are used unmodified in performing those activities but
which are not part of the work.  For example, Corresponding Source
includes interface definition files associated with source files for
the work, and the source code for shared libraries and dynamically
linked subprograms that the work is specifically designed to require,
such as by intimate data communication or control flow between those
subprograms and other parts of the work.

  The Corresponding Source need not include anything that users
can regenerate automatically from other parts of the Corresponding
Source.

  The Corresponding Source for a work in source code form is that
same work.

  2. Basic Permissions.

  All rights granted under this License are granted for the term of
copyright on the Program, and are irrevocable provided the stated
conditions are met.  This License explicitly affirms your unlimited
permission to run the unmodified Program.  The output from running a
covered work is covered by this License only if the output, given its
content, constitutes a covered work.  This License acknowledges your
rights of fair use or other equivalent, as provided by copyright law.

  You may make, run and propagate covered works that you do not
convey, without conditions so long as your license otherwise remains
in force.  You may convey covered works to others for the sole purpose
of having them make modifications exclusively for you, or provide you
with facilities for running those works, provided that you comply with
the terms of this License in conveying all material for which you do
not control copyright.  Those thus making or running the covered works
for you must do so exclusively on your behalf, under your direction
and control, on terms that prohibit them from making any copies of
your copyrighted material outside their relationship with you.

  Conveying under any other circumstances is permitted solely under
the conditions stated below.  Sublicensing is not allowed; section 10
makes it unnecessary.

  3. Protecting Users' Legal Rights From Anti-Circumvention Law.

  No covered work shall be deemed part of an effective technological
measure under any applicable law fulfilling obligations under article
11 of the WIPO copyright treaty adopted on 20 December 1996, or
similar laws prohibiting or restricting circumvention of such
measures.

  When you convey a covered work, you waive any legal power to forbid
circumvention of technological measures to the extent such circumvention
is effected by exercising rights under this License with respect to
the covered work, and you disclaim any intention to limit operation or
modification of the work as a means of enforcing, against the work's
users, your or third parties' legal rights to forbid circumvention of
technological measures.

  4. Conveying Verbatim Copies.

  You may convey verbatim copies of the Program's source code as you
receive it, in any medium, provided that you conspicuously and
appropriately publish on each copy an appropriate copyright notice;
keep intact all notices stating that this License and any
non-permissive terms added in accord with section 7 apply to the code;
keep intact all notices of the absence of any warranty; and give all
recipients a copy of this License along with the Program.

  You may charge any price or no price for each copy that you convey,
and you may offer support or warranty protection for a fee.

  5. Conveying Modified Source Versions.

  You may convey a work based on the Program, or the modifications to
produce it from the Program, in the form of source code under the
terms of section 4, provided that you also meet all of these conditions:

    a) The work must carry prominent notices stating that you modified
    it, and giving a relevant date.

    b) The work must carry prominent notices stating that it is
    released under this License and any conditions added under section
    7.  This requirement modifies the requirement in section 4 to
    "keep intact all notices".

    c) You must license the entire work, as a whole, under this
    License to anyone who comes into possession of a copy.  This
    License will therefore apply, along with any applicable section 7
    additional terms, to the whole of the work, and all its parts,
    regardless of how they are packaged.  This License gives no
    permission to license the work in any other way, but it does not
    invalidate such permission if you have separately received it.

    d) If the work has interactive user interfaces, each must display
    Appropriate Legal Notices; however, if the Program has interactive
    interfaces that do not display Appropriate Legal Notices, your
    work need not make them do so.

  A compilation of a covered work with other separate and independent
works, which are not by their nature extensions of the covered work,
and which are not combined with it such as to form a larger program,
in or on a volume of a storage or distribution medium, is called an
"aggregate" if the compilation and its resulting copyright are not
used to limit the access or legal rights of the compilation's users
beyond what the individual works permit.  Inclusion of a covered work
in an aggregate does not cause this License to apply to the other
parts of the aggregate.

  6. Conveying Non-Source Forms.

  You may convey a covered work in object code form under the terms
of sections 4 and 5, provided that you also convey the
machine-readable Corresponding Source under the terms of this License,
in one of these ways:

    a) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by the
    Corresponding Source fixed on a durable physical medium
    customarily used for software interchange.

    b) Convey the object code in, or embodied in, a physical product
    (including a physical distribution medium), accompanied by a
    written offer, valid for at least three years and valid for as
    long as you offer spare parts or customer support for that product
    model, to give anyone who possesses the object code either (1) a
    copy of the Corresponding Source for all the software in the
    product that is covered by this License, on a durable physical
    medium customarily used for software interchange, for a price no
    more than your reasonable cost of physically performing this
    conveying of source, or (2) access to copy the
    Corresponding Source from a network server at no charge.

    c) Convey individual copies of the object code with a copy of the
    written offer to provide the Corresponding Source.  This
    alternative is allowed only occasionally and noncommercially, and
    only if you received the object code with such an offer, in accord
    with subsection 6b.

    d) Convey the object code by offering access from a designated
    place (gratis or for a charge), and offer equivalent access to the
    Corresponding Source in the same way through the same place at no
    further charge.  You need not require recipients to copy the
    Corresponding Source along with the object code.  If the place to
    copy the object code is a network server, the Corresponding Source
    may be on a different server (operated by you or a third party)
    that supports equivalent copying facilities, provided you maintain
    clear directions next to the object code saying where to find the
    Corresponding Source.  Regardless of what server hosts the
    Corresponding Source, you remain obligated to ensure that it is
    available for as long as needed to satisfy these requirements.

    e) Convey the object code using peer-to-peer transmission, provided
    you inform other peers where the object code and Corresponding
    Source of the work are being offered to the general public at no
    charge under subsection 6d.

  A separable portion of the object code, whose source code is excluded
from the Corresponding Source as a System Library, need not be
included in conveying the object code work.

  A "User Product" is either (1) a "consumer product", which means any
tangible personal property which is normally used for personal, family,
or household purposes, or (2) anything designed or sold for incorporation
into a dwelling.  In determining whether a product is a consumer product,
doubtful cases shall be resolved in favor of coverage.  For a particular
product received by a particular user, "normally used" refers to a
typical or common use of that class of product, regardless of the status
of the particular user or of the way in which the particular user
actually uses, or expects or is expected to use, the product.  A product
is a consumer product regardless of whether the product has substantial
commercial, industrial or non-consumer uses, unless such uses represent
the only significant mode of use of the product.

  "Installation Information" for a User Product means any methods,
procedures, authorization keys, or other information required to install
and execute modified versions of a covered work in that User Product from
a modified version of its Corresponding Source.  The information must
suffice to ensure that the continued functioning of the modified object
code is in no case prevented or interfered with solely because
modification has been made.

  If you convey an object code work under this section in, or with, or
specifically for use in, a User Product, and the conveying occurs as
part of a transaction in which the right of possession and use of the
User Product is transferred to the recipient in perpetuity or for a
fixed term (regardless of how the transaction is characterized), the
Corresponding Source conveyed under this section must be accompanied
by the Installation Information.  But this requirement does not apply
if neither you nor any third party retains the ability to install
modified object code on the User Product (for example, the work has
been installed in ROM).

  The requirement to provide Installation Information does not include a
requirement to continue to provide support service, warranty, or updates
for a work that has been modified or installed by the recipient, or for
the User Product in which it has been modified or installed.  Access to a
network may be denied when the modification itself materially and
adversely affects the operation of the network or violates the rules and
protocols for communication across the network.

  Corresponding Source conveyed, and Installation Information provided,
in accord with this section must be in a format that is publicly
documented (and with an implementation available to the public in
source code form), and must require no special password or key for
unpacking, reading or copying.

  7. Additional Terms.

  "Additional permissions" are terms that supplement the terms of this
License by making exceptions from one or more of its conditions.
Additional permissions that are applicable to the entire Program shall
be treated as though they were included in this License, to the extent
that they are valid under applicable law.  If additional permissions
apply only to part of the Program, that part may be used separately
under those permissions, but the entire Program remains governed by
this License without regard to the additional permissions.

  When you convey a copy of a covered work, you may at your option
remove any additional permissions from that copy, or from any part of
it.  (Additional permissions may be written to require their own
removal in certain cases when you modify the work.)  You may place
additional permissions on material, added by you to a covered work,
for which you have or can give appropriate copyright permission.

  Notwithstanding any other provision of this License, for material you
add to a covered work, you may (if authorized by the copyright holders of
that material) supplement the terms of this License with terms:

    a) Disclaiming warranty or limiting liability differently from the
    terms of sections 15 and 16 of this License; or

    b) Requiring preservation of specified reasonable legal notices or
    author attributions in that material or in the Appropriate Legal
    Notices displayed by works containing it; or

    c) Prohibiting misrepresentation of the origin of that material, or
    requiring that modified versions of such material be marked in
    reasonable ways as different from the original version; or

    d) Limiting the use for publicity purposes of names of licensors or
    authors of the material; or

    e) Declining to grant rights under trademark law for use of some
    trade names, trademarks, or service marks; or

    f) Requiring indemnification of licensors and authors of that
    material by anyone who conveys the material (or modified versions of
    it) with contractual assumptions of liability to the recipient, for
    any liability that these contractual assumptions directly impose on
    those licensors and authors.

  All other non-permissive additional terms are considered "further
restrictions" within the meaning of section 10.  If the Program as you
received it, or any part of it, contains a notice stating that it is
governed by this License along with a term that is a further
restriction, you may remove that term.  If a license document contains
a further restriction but permits relicensing or conveying under this
License, you may add to a covered work material governed by the terms
of that license document, provided that the further restriction does
not survive such relicensing or conveying.

  If you add terms to a covered work in accord with this section, you
must place, in the relevant source files, a statement of the
additional terms that apply to those files, or a notice indicating
where to find the applicable terms.

  Additional terms, permissive or non-permissive, may be stated in the
form of a separately written license, or stated as exceptions;
the above requirements apply either way.

  8. Termination.

  You may not propagate or modify a covered work except as expressly
provided under this License.  Any attempt otherwise to propagate or
modify it is void, and will automatically terminate your rights under
this License (including any patent licenses granted under the third
paragraph of section 11).

  However, if you cease all violation of this License, then your
license from a particular copyright holder is reinstated (a)
provisionally, unless and until the copyright holder explicitly and
finally terminates your license, and (b) permanently, if the copyright
holder fails to notify you of the violation by some reasonable means
prior to 60 days after the cessation.

  Moreover, your license from a particular copyright holder is
reinstated permanently if the copyright holder notifies you of the
violation by some reasonable means, this is the first time you have
received notice of violation of this License (for any work) from that
copyright holder, and you cure the violation prior to 30 days after
your receipt of the notice.

  Termination of your rights under this section does not terminate the
licenses of parties who have received copies or rights from you under
this License.  If your rights have been terminated and not permanently
reinstated, you do not qualify to receive new licenses for the same
material under section 10.

  9. Acceptance Not Required for Having Copies.

  You are not required to accept this License in order to receive or
run a copy of the Program.  Ancillary propagation of a covered work
occurring solely as a consequence of using peer-to-peer transmission
to receive a copy likewise does not require acceptance.  However,
nothing other than this License grants you permission to propagate or
modify any covered work.  These actions infringe copyright if you do
not accept this License.  Therefore, by modifying or propagating a
covered work, you indicate your acceptance of this License to do so.

  10. Automatic Licensing of Downstream Recipients.

  Each time you convey a covered work, the recipient automatically
receives a license from the original licensors, to run, modify and
propagate that work, subject to this License.  You are not responsible
for enforcing compliance by third parties with this License.

  An "entity transaction" is a transaction transferring control of an
organization, or substantially all assets of one, or subdividing an
organization, or merging organizations.  If propagation of a covered
work results from an entity transaction, each party to that
transaction who receives a copy of the work also receives whatever
licenses to the work the party's predecessor in interest had or could
give under the previous paragraph, plus a right to possession of the
Corresponding Source of the work from the predecessor in interest, if
the predecessor has it or can get it with reasonable efforts.

  You may not impose any further restrictions on the exercise of the
rights granted or affirmed under this License.  For example, you may
not impose a license fee, royalty, or other charge for exercise of
rights granted under this License, and you may not initiate litigation
(including a cross-claim or counterclaim in a lawsuit) alleging that
any patent claim is infringed by making, using, selling, offering for
sale, or importing the Program or any portion of it.

  11. Patents.

  A "contributor" is a copyright holder who authorizes use under this
License of the Program or a work on which the Program is based.  The
work thus licensed is called the contributor's "contributor version".

  A contributor's "essential patent claims" are all patent claims
owned or controlled by the contributor, whether already acquired or
hereafter acquired, that would be infringed by some manner, permitted
by this License, of making, using, or selling its contributor version,
but do not include claims that would be infringed only as a
consequence of further modification of the contributor version.  For
purposes of this definition, "control" includes the right to grant
patent sublicenses in a manner consistent with the requirements of
this License.

  Each contributor grants you a non-exclusive, worldwide, royalty-free
patent license under the contributor's essential patent claims, to
make, use, sell, offer for sale, import and otherwise run, modify and
propagate the contents of its contributor version.

  In the following three paragraphs, a "patent license" is any express
agreement or commitment, however denominated, not to enforce a patent
(such as an express permission to practice a patent or covenant not to
sue for patent infringement).  To "grant" such a patent license to a
party means to make such an agreement or commitment not to enforce a
patent against the party.

  If you convey a covered work, knowingly relying on a patent license,
and the Corresponding Source of the work is not available for anyone
to copy, free of charge and under the terms of this License, through a
publicly available network server or other readily accessible means,
then you must either (1) cause the Corresponding Source to be so
available, or (2) arrange to deprive yourself of the benefit of the
patent license for this particular work, or (3) arrange, in a manner
consistent with the requirements of this License, to extend the patent
license to downstream recipients.  "Knowingly relying" means you have
actual knowledge that, but for the patent license, your conveying the
covered work in a country, or your recipient's use of the covered work
in a country, would infringe one or more identifiable patents in that
country that you have reason to believe are valid.
  
  If, pursuant to or in connection with a single transaction or
arrangement, you convey, or propagate by procuring conveyance of, a
covered work, and grant a patent license to some of the parties
receiving the covered work authorizing them to use, propagate, modify
or convey a specific copy of the covered work, then the patent license
you grant is automatically extended to all recipients of the covered
work and works based on it.

  A patent license is "discriminatory" if it does not include within
the scope of its coverage, prohibits the exercise of, or is
conditioned on the non-exercise of one or more of the rights that are
specifically granted under this License.  You may not convey a covered
work if you are a party to an arrangement with a third party that is
in the business of distributing software, under which you make payment
to the third party based on the extent of your activity of conveying
the work, and under which the third party grants, to any of the
parties who would receive the covered work from you, a discriminatory
patent license (a) in connection with copies of the covered work
conveyed by you (or copies made from those copies), or (b) primarily
for and in connection with specific products or compilations that
contain the covered work, unless you entered into that arrangement,
or that patent license was granted, prior to 28 March 2007.

  Nothing in this License shall be construed as excluding or limiting
any implied license or other defenses to infringement that may
otherwise be available to you under applicable patent law.

  12. No Surrender of Others' Freedom.

  If conditions are imposed on you (whether by court order, agreement or
otherwise) that contradict the conditions of this License, they do not
excuse you from the conditions of this License.  If you cannot convey a
covered work so as to satisfy simultaneously your obligations under this
License and any other pertinent obligations, then as a consequence you may
not convey it at all.  For example, if you agree to terms that obligate you
to collect a royalty for further conveying from those to whom you convey
the Program, the only way you could satisfy both those terms and this
License would be to refrain entirely from conveying the Program.

  13. Use with the GNU Affero General Public License.

  Notwithstanding any other provision of this License, you have
permission to link or combine any covered work with a work licensed
under version 3 of the GNU Affero General Public License into a single
combined work, and to convey the resulting work.  The terms of this
License will continue to apply to the part which is the covered work,
but the special requirements of the GNU Affero General Public License,
section 13, concerning interaction through a network will apply to the
combination as such.

  14. Revised Versions of this License.

  The Free Software Foundation may publish revised and/or new versions of
the GNU General Public License from time to time.  Such new versions will
be similar in spirit to the present version, but may differ in detail to
address new problems or concerns.

  Each version is given a distinguishing version number.  If the
Program specifies that a certain numbered version of the GNU General
Public License "or any later version" applies to it, you have the
option of following the terms and conditions either of that numbered
version or of any later version published by the Free Software
Foundation.  If the Program does not specify a version number of the
GNU General Public License, you may choose any version ever published
by the Free Software Foundation.

  If the Program specifies that a proxy can decide which future
versions of the GNU General Public License can be used, that proxy's
public statement of acceptance of a version permanently authorizes you
to choose that version for the Program.

  Later license versions may give you additional or different
permissions.  However, no additional obligations are imposed on any
author or copyright holder as a result of your choosing to follow a
later version.

  15. Disclaimer of Warranty.

  THERE IS NO WARRANTY FOR THE PROGRAM, TO THE EXTENT PERMITTED BY
APPLICABLE LAW.  EXCEPT WHEN OTHERWISE STATED IN WRITING THE COPYRIGHT
HOLDERS AND/OR OTHER PARTIES PROVIDE THE PROGRAM "AS IS" WITHOUT WARRANTY
OF ANY KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE.  THE ENTIRE RISK AS TO THE QUALITY AND PERFORMANCE OF THE PROGRAM
IS WITH YOU.  SHOULD THE PROGRAM PROVE DEFECTIVE, YOU ASSUME THE COST OF
ALL NECESSARY SERVICING, REPAIR OR CORRECTION.

  16. Limitation of Liability.

  IN NO EVENT UNLESS REQUIRED BY APPLICABLE LAW OR AGREED TO IN WRITING
WILL ANY COPYRIGHT HOLDER, OR ANY OTHER PARTY WHO MODIFIES AND/OR CONVEYS
THE PROGRAM AS PERMITTED ABOVE, BE LIABLE TO YOU FOR DAMAGES, INCLUDING ANY
GENERAL, SPECIAL, INCIDENTAL OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE
USE OR INABILITY TO USE THE PROGRAM (INCLUDING BUT NOT LIMITED TO LOSS OF
DATA OR DATA BEING RENDERED INACCURATE OR LOSSES SUSTAINED BY YOU OR THIRD
PARTIES OR A FAILURE OF THE PROGRAM TO OPERATE WITH ANY OTHER PROGRAMS),
EVEN IF SUCH HOLDER OR OTHER PARTY HAS BEEN ADVISED OF THE POSSIBILITY OF
SUCH DAMAGES.

  17. Interpretation of Sections 15 and 16.

  If the disclaimer of warranty and limitation of liability provided
above cannot be given local legal effect according to their terms,
reviewing courts shall apply local law that most closely approximates
an absolute waiver of all civil liability in connection with the
Program, unless a warranty or assumption of liability accompanies a
copy of the Program in return for a fee.

		     END OF TERMS AND CONDITIONS

	    How to Apply These Terms to Your New Programs

  If you develop a new program, and you want it to be of the greatest
possible use to the public, the best way to achieve this is to make it
free software which everyone can redistribute and change under these terms.

  To do so, attach the following notices to the program.  It is safest
to attach them to the start of each source file to most effectively
state the exclusion of warranty; and each file should have at least
the "copyright" line and a pointer to where the full notice is found.

    <one line to give the program's name and a brief idea of what it does.>
    Copyright (C) <year>  <name of author>

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

Also add information on how to contact you by electronic and paper mail.

  If the program does terminal interaction, make it output a short
notice like this when it starts in an interactive mode:

    <program>  Copyright (C) <year>  <name of author>
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<http://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<http://www.gnu.org/philosophy/why-not-lgpl.html>.




================================================
FILE: format_code.sh
================================================
#!/usr/bin/bash

files=(
"src/installer/kiwix-install.cpp"
"src/searcher/kiwix-search.cpp"
"src/manager/kiwix-manage.cpp"
"src/server/kiwix-serve.cpp"
)

for i in "${files[@]}"
do
  echo $i
  clang-format -i -style=file $i
done



================================================
FILE: meson.build
================================================
project('kiwix-tools', 'cpp',
  version : '3.8.2',
  license : 'GPL',
  default_options: ['c_std=c11', 'cpp_std=c++17', 'werror=true'])

compiler = meson.get_compiler('cpp')

add_global_arguments('-DKIWIX_TOOLS_VERSION="@0@"'.format(meson.project_version()), language : 'cpp')

if host_machine.system() == 'windows'
  add_project_arguments('-DNOMINMAX', language: 'cpp')
endif

static_linkage = get_option('static-linkage')
if static_linkage
  # Static build is not supported on MacOS
  if host_machine.system() != 'darwin'
    add_global_link_arguments('-static-libstdc++', '--static', language:'cpp')
  endif
endif

thread_dep = dependency('threads')
libzim_dep = dependency('libzim', version:['>=9.0.0', '<10.0.0'], static:static_linkage)
libkiwix_dep = dependency('libkiwix', version:['>=14.1.0', '<15.0.0'], static:static_linkage)
libdocopt_dep = dependency('docopt', static:static_linkage)

all_deps = [thread_dep, libkiwix_dep, libzim_dep, libdocopt_dep]

if static_linkage
  librt = compiler.find_library('rt', required:false)
  if librt.found()
    all_deps += librt
  endif
endif

subdir('src')
if get_option('doc')
  subdir('docs')
endif



================================================
FILE: meson_options.txt
================================================
option('static-linkage', type : 'boolean', value : false,
  description : 'Create statically linked binaries.')
option('doc', type : 'boolean', value : false,
  description : 'Build the documentations.')



================================================
FILE: .clang-format
================================================
BasedOnStyle:  Google
BinPackArguments: false
BinPackParameters: false
BreakBeforeBinaryOperators: All
BreakBeforeBraces: Linux
DerivePointerAlignment: false
SpacesInContainerLiterals: false
Standard: Cpp11

AllowShortFunctionsOnASingleLine: Inline
AllowShortIfStatementsOnASingleLine: false
AllowShortLoopsOnASingleLine: false



================================================
FILE: .readthedocs.yaml
================================================
# Read the Docs configuration file
# See https://docs.readthedocs.io/en/stable/config-file/v2.html for details

# Required
version: 2

# Set the version of Python and other tools you might need
build:
  os: ubuntu-22.04
  tools:
    python: "3.11"

# Build documentation in the docs/ directory with Sphinx
sphinx:
  configuration: docs/conf.py

# We recommend specifying your dependencies to enable reproducible builds:
# https://docs.readthedocs.io/en/stable/guides/reproducible-builds.html
python:
  install:
  - requirements: docs/requirements.txt



================================================
FILE: debian/changelog
================================================
kiwix-tools (0.0.0) unstable; urgency=medium

  * Initial release

 -- Kunal Mehta <legoktm@debian.org>  Mon, 13 Jul 2020 17:21:11 -0700



================================================
FILE: debian/control
================================================
Source: kiwix-tools
Section: utils
Priority: optional
Maintainer: Kiwix team <kiwix@kiwix.org>
Build-Depends: debhelper-compat (= 13),
               libzim-dev (>= 9.0), libzim-dev (<< 10.0),
               libkiwix-dev (>= 14.0), libkiwix-dev (<< 15.0),
               cmake,
               libdocopt-dev,
               meson,
               pkgconf,
Standards-Version: 4.6.2
Homepage: https://github.com/kiwix/kiwix-tools
Rules-Requires-Root: no

Package: kiwix-tools
Architecture: any
Depends: ${misc:Depends}, ${shlibs:Depends}
Description: collection of Kiwix tools
 kiwix-tools is a collection of various command-line tools used to help
 users interact with and manage ZIM files. It includes:
  * kiwix-serve is a standalone HTTP server for serving ZIM files
    over the network.
  * kiwix-manage allows one to manage the content of the Kiwix library (an
    XML file listing available ZIM files).
  * kiwix-search allows one to find articles in a ZIM file using fulltext
    search patterns.



================================================
FILE: debian/copyright
================================================
See COPYING in the repository root.



================================================
FILE: debian/rules
================================================
#!/usr/bin/make -f
export DEB_BUILD_MAINT_OPTIONS = hardening=+all

%:
	dh $@



================================================
FILE: debian/source/format
================================================
3.0 (native)



================================================
FILE: docker/README.md
================================================
Kiwix-tools Docker image
===

- Available on [ghcr.io](https://ghcr.io/kiwix/kiwix-tools).
- multi-arch (`linux/amd64`, `linux/arm64`, `linux/arm/v7`)
- based on official `kiwix-tools` binaries.

## Usage

``` sh
$ docker run -it ghcr.io/kiwix/kiwix-tools:3.1.2

Welcome to kiwix-tools! The following binaries are available:
kiwix-manage  kiwix-search  kiwix-serve
```

`kiwix-tools` operates on zim files. You shall mount a volume to access the files.

```sh
docker run -v $(pwd):/data -it ghcr.io/kiwix/kiwix-tools kiwix-search /data/wikipedia_fr_test.zim "Mali"
```

## Building and reusing

- `kiwix/kiwix-tools` is multi-arch and is ideally built using `buildx`.
- requires a `--build-arg VERSION=` with the kiwix-tools release.
- can be built using `docker build` in which case it expects an additionnal `--build-arg ARCH=arm` for arm. Otherwise defaults to `amd64`.

**Notes:**

- `wget` in `alpine:3` on `arm/v7` (__inside github action only__) crashes when downloading from HTTPs locations. Keep http-only in Dockerfile.
- Was also unhappy when using the mirrors so it's using `mirror.download` on purpose.

## See also

If you are interested by a Kiwix server only container image, [here it is](server/README.md).


================================================
FILE: docker/Dockerfile
================================================
FROM alpine:3.22
LABEL org.opencontainers.image.source=https://github.com/openzim/kiwix-tools

# TARGETPLATFORM is injected by docker build
ARG TARGETPLATFORM
ARG VERSION

RUN set -e && \
    apk --no-cache add dumb-init curl && \
    echo "TARGETPLATFORM: $TARGETPLATFORM" && \
    if [ "$TARGETPLATFORM" = "linux/386" ]; then ARCH="i586"; \
    # linux/arm64/v8 points to linux/arm64
    elif [ "$TARGETPLATFORM" = "linux/arm64/v8" \
        -o "$TARGETPLATFORM" = "linux/arm64" ]; then ARCH="aarch64"; \
    # linux/arm translates to linux/arm/v7
    elif [ "$TARGETPLATFORM" = "linux/arm/v7" ]; then ARCH="armv8"; \
    elif [ "$TARGETPLATFORM" = "linux/arm/v6" ]; then ARCH="armv6"; \
    elif [ "$TARGETPLATFORM" = "linux/amd64/v3" \
        -o "$TARGETPLATFORM" = "linux/amd64/v2" \
        -o "$TARGETPLATFORM" = "linux/amd64" ]; then ARCH="x86_64"; \
    # we dont suppot any other arch so let it fail
    else ARCH="unknown"; fi && \
    # download requested kiwix-tools version
    url="http://mirror.download.kiwix.org/release/kiwix-tools/kiwix-tools_linux-$ARCH-$VERSION.tar.gz" && \
    echo "URL: $url" && \
    curl -k -L $url | tar -xz -C /usr/local/bin/ --strip-components 1 && \
    # only needed in dockerfile
    apk del curl

# expose kiwix-serve default port
EXPOSE 80

ENTRYPOINT ["/usr/bin/dumb-init", "--"]
CMD ["/bin/sh", "-c", "echo 'Welcome to kiwix-tools! The following binaries are available:' && ls /usr/local/bin/"]



================================================
FILE: docker/server/README.md
================================================
Kiwix serve Docker image
========================

With local ZIM file(s)
----------------------

* Download a ZIM file from <https://wiki.kiwix.org/wiki/Content>

* Given `wikipedia.zim` and `wiktionary.zim` reside in `/tmp/zim/`, execute the following:

```bash
docker run -v /tmp/zim:/data -p 8080:8080 ghcr.io/kiwix/kiwix-serve wikipedia.zim wiktionary.zim
```

or, if you want to load all ZIM files within a directory, then use globbing:

```bash
docker run -v /tmp/zim:/data -p 8080:8080 ghcr.io/kiwix/kiwix-serve '*.zim'
```

With remote ZIM file
--------------------

```bash
docker run -e "DOWNLOAD=https://download.kiwix.org/zim/wikipedia_bm_all.zim" -p 8080:8080 ghcr.io/kiwix/kiwix-serve
```

Change default port
-------------------

You can change port to expose with environment variable PORT, useful if running on Podman, K8s or OpenShift

```bash
podman run -e "DOWNLOAD=https://download.kiwix.org/zim/wikipedia_bm_all.zim" -e PORT=8888 -p 8080:8888 ghcr.io/kiwix/kiwix-serve
```

ARM
---

Build an image for an ARM based GNU/Linux:
```bash
docker build . -t ghcr.io/kiwix/kiwix-serve:latest --build-arg ARCH="arm32v7/"
```

Docker Compose
--------------

You can also deploy kiwix with
[`docker-compose`](https://docs.docker.com/compose/). Check out a
sample at [docker-compose.yml.example](docker-compose.yml.example).

Screenshots
-----------

![screenshot_1.png](https://github.com/kiwix/kiwix-tools/raw/master/docker/server/pictures/screenshot_1.png)
![screenshot_2.png](https://github.com/kiwix/kiwix-tools/raw/master/docker/server/pictures/screenshot_2.png)



================================================
FILE: docker/server/docker-compose.yml.example
================================================
version: '3.3'
services:
  kiwix-serve:
      ports:
        - 8080:8080
      image: ghcr.io/kiwix/kiwix-serve:latest
      # uncomment next 4 lines to use it with local zim file in /tmp/zim
      # volumes:
      #   - /tmp/zim:/data
      # command:
      #   - '*.zim'
      # uncomment next 2 lines to use it with remote zim file
      # environment:
      #   - 'DOWNLOAD=https://download.kiwix.org/zim/wikipedia_bm_all.zim'



================================================
FILE: docker/server/Dockerfile
================================================
ARG VERSION=latest

# kiwix-tools is multi-arch
FROM ghcr.io/kiwix/kiwix-tools:$VERSION
LABEL org.opencontainers.image.source=https://github.com/openzim/kiwix-tools

# expose kiwix-serve default port and workdir
EXPOSE 8080
VOLUME /data
WORKDIR /data

# running as a named unprivileged user
RUN addgroup -S -g 1001 user && adduser -S -u 1001 user -G user
RUN chown user:user /data
USER user

COPY ./start.sh /usr/local/bin/

ENTRYPOINT ["/usr/bin/dumb-init", "--", "/usr/local/bin/start.sh"]



================================================
FILE: docker/server/start.sh
================================================
#!/bin/sh

# Download if necessary a file
if [ ! -z "$DOWNLOAD" ]
then
    # Check if /data is writable
    if [ ! -w /data ]
    then
        echo "'/data' directory is not writable by '$(id -n -u):$(id -n -g)' ($(id -u):$(id -g)). ZIM file(s) can not be written."
        exit 1
    fi

    # Dwonload ZIM file
    ZIM=`basename $DOWNLOAD`
    wget $DOWNLOAD -O "$ZIM"

    # Set arguments
    if [ "$#" -eq "0" ]
    then
        set -- "$@" $ZIM
    fi
fi

if [ -z "$PORT" ]
then
    PORT=8080
fi
CMD="/usr/local/bin/kiwix-serve --port=$PORT $@"
echo $CMD
$CMD

# If error, print the content of /data
if [ $? -ne 0 ]
then
    echo "Here is the content of /data:"
    find /data -type f
fi



================================================
FILE: docs/conf.py
================================================
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'kiwix-tools'
copyright = '2024, kiwix-team'
author = 'kiwix-team'


# -- General configuration ---------------------------------------------------

on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
        "sphinx_rtd_theme"
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []



================================================
FILE: docs/index.rst
================================================
Welcome to kiwix-tools' documentation!
======================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   kiwix-serve



================================================
FILE: docs/kiwix-serve.rst
================================================
***********
kiwix-serve
***********

Introduction
============

``kiwix-serve`` is a tool for serving ZIM file content over HTTP. It supports
serving a library containing multiple ZIM files. In a large library served by a
``kiwix-serve`` instance clients can look up/filter ZIM files of interest by
words in their :term:`titles <ZIM title>` and/or descriptions, language, tags, etc.

``kiwix-serve`` provides a ZIM file viewer for displaying inidividual pages
from a ZIM file inside the user's web browser (without downloading the full ZIM
file).

Clients can also remotely search inside those ZIM files that contain a full-text
search database.

``kiwix-serve`` supports Web browsers `Firefox >= 70, Chrome >= 80, Edge >= 80, ChromeAndroid >= 80, Safari >= 14, iOS >= 14 <https://browsersl.ist/#q=Firefox+%3E%3D+70%2C+Chrome+%3E%3D+80%2C+Edge+%3E%3D+80%2C+ChromeAndroid+%3E%3D+80%2C+Safari+%3E%3D+14%2C+iOS+%3E%3D+14>`_.

Usage
=====

.. code-block:: sh

  kiwix-serve --library [OPTIONS] LIBRARY_FILE_PATH
  kiwix-serve [OPTIONS] ZIM_FILE_PATH ...


Arguments
---------

.. _cli-arg-library-file-path:

``LIBRARY_FILE_PATH``: path of an XML library file listing ZIM files to serve.
To be used only with the :option:`--library` option. Multiple library files can
be provided as a semicolon (``;``) separated list.

``ZIM_FILE_PATH``: ZIM file path (multiple arguments are allowed).

Options
-------

.. option:: --library

  By default, ``kiwix-serve`` expects a list of ZIM files as command line
  arguments. Providing the :option:`--library` option tells ``kiwix-serve``
  that the command line argument is rather a :ref:`library XML file
  <cli-arg-library-file-path>`.

.. option:: --catalogOnly

  In this mode ``kiwix-serve`` only serves the welcome (library) page and the
  OPDS catalog. ZIM files referred by the :ref:`library XML file
  <cli-arg-library-file-path>` need not be accessible.

  This option may be combined with the :option:`--contentServerURL` option.

.. option:: --contentServerURL=URL

  In :option:`--catalogOnly` mode book content is not served by this instance
  of `kiwix-serve`. If a separate instance of `kiwix-serve` is running for the
  same library without that option and thus serves book content, then the root
  URL of that server can be passed to this instance so that books can still be
  previewed.

  This option must be combined with the :option:`--catalogOnly` option.

.. option:: -i ADDR, --address=ADDR

  Listen only on this IP address. By default the server listens on all
  available IP addresses. Alternatively, you can use special values to define which types of connections to accept:

  - all : Listen for connections on all IP addresses (IPv4 and IPv6).
  - ipv4 : Listen for connections on all IPv4 addresses.
  - ipv6 : Listen for connections on all IPv6 addresses.


.. option:: -p PORT, --port=PORT

  TCP port on which to listen for HTTP requests (default: 80).


.. option:: -r ROOT, --urlRootLocation=ROOT

  URL prefix on which the content should be made available (default: empty).


.. option:: -d, --daemon

  Detach the HTTP server daemon from the main process.


.. option:: -a PID, --attachToProcess=PID

  Exit when the process with id PID stops running.


.. option:: -M, --monitorLibrary

  Monitor the XML library file and reload it automatically when it changes.

  Library reloading can be forced anytime by sending a SIGHUP signal to the
  ``kiwix-serve`` process (this works regardless of the presence of the
  :option:`--monitorLibrary`/:option:`-M` option).


.. option:: -m, --nolibrarybutton

  Disable the library home button in the ZIM viewer toolbar.


.. option:: -n, --nosearchbar

  Disable the searchbox in the ZIM viewer toolbar.


.. option:: -b, --blockexternal

  Prevent the users from directly navigating to external resources via such
  links in ZIM content.


.. option:: -t N, --threads=N

  Number of threads to run in parallel (default: 4).


.. option:: -s N, --searchLimit=N

  Maximum number of ZIM files in a fulltext multizim search (default: No limit).


.. option:: -z, --nodatealiases

  Create URL aliases for each content by removing the date embedded in the file
  name. The expected format of the date in the filename is ``_YYYY-MM``. For
  example, ZIM file ``wikipedia_en_all_2020-08.zim`` will be accessible both as
  ``wikipedia_en_all_2020-08`` and ``wikipedia_en_all``.


.. option:: -c PATH, --customIndex=PATH

  Override the welcome page with a custom HTML file.


.. option:: -L N, --ipConnectionLimit=N

  Max number of (concurrent) connections per IP (default: infinite,
  recommended: >= 6).


.. option:: -v, --verbose

  Print debug log to STDOUT.


.. option:: -V, --version

  Print the software version.


.. option:: -h, --help

  Print the help text.


HTTP API
========

``kiwix-serve`` serves content at/under ``http://ADDR:PORT/ROOT`` where
``ADDR``, ``PORT`` and ``ROOT`` are the values supplied to the
:option:`--address`/:option:`-i`, :option:`--port`/:option:`-p` and
:option:`--urlRootLocation`/:option:`-r` options, respectively.

HTTP API endpoints presented below are relative to that location, i.e.
``/foo/bar`` must be actually accessed as ``http://ADDR:PORT/ROOT/foo/bar``.

.. note::

  The HTTP API is documented in its entirety in order to facilitate the work of
  the Kiwix development team. Note, however, that only a subset of the HTTP API
  constitutes ``kiwix-serves``'s public interface.

  .. _public-api-endpoint:

  **Public API endpoint**

    A public HTTP API endpoint is intended to serve the outside world (in
    addition to ``kiwix-serve``'s front-end and other Kiwix products). The
    Kiwix development team will do its best to ensure gratifying experience for
    clients of public API endpoints at all stages of the endpoint lifecycle.

  .. _private-api-endpoint:

  **Private API endpoint**

    A private API endpoint is intended to be used only by ``kiwix-serve``'s
    frontend or by other products maintained solely by the Kiwix team. Private
    API comes without any guaranees. It may change as frequently and as
    drasticaly as the Kiwix development team sees fit.

  .. _deprecation:

  **Deprecation**

    Public API doesn't stay frozen once and forever. As the API evolves, Kiwix
    team reserves the right to drop support for certain old functionality. In
    such events, an advance notice will be issued and the users will be given
    enough time to prepare for the change.

  Currently, public endpoints are limited to the following list:

    -  :ref:`OPDS API <new-opds-api>`
    -  ``/raw``
    -  ``/search`` (with ``/search/searchdescription.xml``)

.. _welcome-page:

``/``
-----

===== ===========
Type: :ref:`private <private-api-endpoint>`
===== ===========

Welcome page is served under ``/``. By default this is the library page, where
books are listed and can be looked up/filtered interactively. However, the
welcome page can be overriden through the :option:`--customIndex`/:option:`-c`
command line option of ``kiwix-serve``.


.. _new-opds-api:

``/catalog/v2`` (OPDS API)
------------------------------

===== ===========
Type: :ref:`public <public-api-endpoint>`
===== ===========

The new OPDS API of ``kiwix-serve`` is based on the `OPDS Catalog specification
v1.2 <https://specs.opds.io/opds-1.2>`_. All of its endpoints are grouped under
``/catalog/v2``.

:ref:`Legacy OPDS API <legacy-opds-api>` is preserved for backward
compatibility.


``/catalog/v2/root.xml``
^^^^^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: member of a :ref:`public API <new-opds-api>`
===== ===========

The OPDS Catalog Root links to the OPDS acquisition and navigation feeds
accessible through the other endpoints of the OPDS API.


``/catalog/v2/searchdescription.xml``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: member of a :ref:`public API <new-opds-api>`
===== ===========

Describes the `/catalog/v2/entries`_ endpoint in `OpenSearch description format
<https://developer.mozilla.org/en-US/docs/Web/OpenSearch>`_.



``/catalog/v2/categories``
^^^^^^^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: member of a :ref:`public API <new-opds-api>`
===== ===========

Returns the full list of ZIM file categories as an `OPDS Navigation Feed
<https://specs.opds.io/opds-1.2#22-navigation-feeds>`_.


``/catalog/v2/entries``
^^^^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: member of a :ref:`public API <new-opds-api>`
===== ===========

Returns a full or filtered list of ZIM files as a paginated `OPDS acquisition
feed <https://specs.opds.io/opds-1.2#23-acquisition-feeds>`_ with `complete
entries
<https://specs.opds.io/opds-1.2#512-partial-and-complete-catalog-entries>`_.

**Pagination:**

By default, no more than 10 first entries are returned from the library. To
obtain the remaining entries the URL query parameters ``start`` and/or
``count`` must be used. The output of ``/catalog/v2/entries?start=s&count=n``
will contain at most ``n`` (default value: 10) results starting from entry #
``s`` (default value: 0).  ``count`` with a negative value (e.g.  ``count=-1``)
removes the limit on the number of results in the output.


.. note::

  Previously ``count=0`` also designated an unbounded query (i.e. worked
  similarly to ``count=-1``). The response to a ``count=0`` query was changed
  to consist of 0 results, as such a query/response combination is a good way
  to find out the total number of results (when only that information is
  needed) with minimal consumption of resources.

Examples:

.. code:: sh

  # Returns the first 10 entries (internally numbered 0 through 9)
  $ curl 'http://localhost:8080/catalog/v2/entries'

  # Returns the next 10 entries (internally numbered 10 through 19)
  $ curl 'http://localhost:8080/catalog/v2/entries?start=10'

  # Returns the first 50 entries
  $ curl 'http://localhost:8080/catalog/v2/entries?count=50'

  # Returns 50 entries starting from entry # 100 (i.e. entries ## 100-149)
  $ curl 'http://localhost:8080/catalog/v2/entries?start=100&count=50'

  # Returns all entries
  $ curl 'http://localhost:8080/catalog/v2/entries?count=-1'

  # Returns all entries starting from entry # 100
  $ curl 'http://localhost:8080/catalog/v2/entries?start=100&count=-1'


.. _library-filtering:

**Filtering:**

A filtered subset of the library can be requested by providing one or more
filtering criteria, whereupon only entries matching *all* of the criteria are
included in the response. Pagination is applied to the filtered list. The
filtering criteria must be specified via the following URL parameters:

* ``lang`` - filter by language (specified as a 3-letter language code).
  Multiple languages can be provided as a comma-separated list. An entry will
  be considered to match this criterion if its language list intersects (in set
  theory sense) with the list of the filter.

  .. note::

     An entry may have multiple languages listed in its metadata. The ``lang``
     filter only allows to select entries by one of those languages. For
     example, ``lang=vol,epo`` selects entries that match *either* ``vol`` *or*
     ``epo`` rather than entries that contain *both* ``vol`` and ``epo`` in
     their language list.

* ``category`` - filter by categories associated with the library entries.
  Multiple categories can be provided as a comma-separated list. An entry will
  be considered to match this criterion if its category matches *any* of the
  requested categories.

* ``tag`` - filter by tags associated with the library entries. Multiple tags
  can be provided as a semicolon separated list (e.g
  ``tag=wikipedia;_videos:no``). The result will contain only those entries
  that contain *all* of the requested tags.

* ``notag`` - filter out (exclude) entries with *any* of the specified tags
  (example - ``notag=ted;youtube``).

* ``maxsize`` - include in the results only entries whose size (in bytes)
  doesn't exceed the provided value.

* ``q`` - include in the results only entries that contain the specified text
  in the title or description.

* ``name`` - include in the results only entries with a matching
  :term:`book name <Book name>`.


Examples:

.. code:: sh

  # List only books in Italian (lang=ita) but
  # return only results ## 100-149 (start=100&count=50)
  $ curl 'http://localhost:8080/catalog/v2/entries?lang=ita&start=100&count=50'

  # List only books in Italian OR French. Return only the first 10 results.
  $ curl 'http://localhost:8080/catalog/v2/entries?lang=ita,fra'

  # List only books with category of 'gutenberg' OR 'wikibooks'.
  # Return only the first 10 results.
  $ curl 'http://localhost:8080/catalog/v2/entries?category=gutenberg,wikibooks'

  # List only books with category of 'wikipedia' AND containing the word
  # 'science' in the title or description. Return only the first 10 results.
  $ curl 'http://localhost:8080/catalog/v2/entries?q=science&category=wikipedia'


``/catalog/v2/entry/ZIMID``
^^^^^^^^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: member of a :ref:`public API <new-opds-api>`
===== ===========

Returns full info about the library entry with :term:`UUID <ZIM UUID>`
``ZIMID``.


``/catalog/v2/illustration/ZIMID``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: member of a :ref:`public API <new-opds-api>`
===== ===========

**Usage:**

  ``/catalog/v2/illustration/ZIMID?size=N``

Returns the illustration of size ``NxN`` pixels for the library entry with
:term:`UUID <ZIM UUID>` ``ZIMID``.

If no illustration of requested size is found a HTTP 404 error is returned.


``/catalog/v2/languages``
^^^^^^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: member of a :ref:`public API <new-opds-api>`
===== ===========

Returns the full list of ZIM file languages as an `OPDS Navigation Feed
<https://specs.opds.io/opds-1.2#22-navigation-feeds>`_.


``/catalog/v2/partial_entries``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: member of a :ref:`public API <new-opds-api>`
===== ===========

Returns the full or filtered list of ZIM files as an `OPDS acquisition feed
<https://specs.opds.io/opds-1.2#23-acquisition-feeds>`_ with `partial entries
<https://specs.opds.io/opds-1.2#512-partial-and-complete-catalog-entries>`_.

Supported filters are the same as for the `/catalog/v2/entries`_ endpoint.


.. _legacy-opds-api:

``/catalog`` (Legacy OPDS API)
------------------------------

===== ===========
Type: :ref:`deprecated <deprecation>`
===== ===========

The legacy OPDS API is preserved for backward compatibility and is deprecated.
:ref:`New OPDS API <new-opds-api>` should be used instead.


``/catalog/root.xml``
^^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: member of a :ref:`deprecated API <legacy-opds-api>`
===== ===========

Full library OPDS catalog (list of all ZIM files).


``/catalog/searchdescription.xml``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: member of a :ref:`deprecated API <legacy-opds-api>`
===== ===========

Describes the `/catalog/search`_ endpoint in `OpenSearch description format
<https://developer.mozilla.org/en-US/docs/Web/OpenSearch>`_.


``/catalog/search``
^^^^^^^^^^^^^^^^^^^

===== ===========
Type: member of a :ref:`deprecated API <legacy-opds-api>`
===== ===========

Returns the list of ZIM files (in OPDS catalog format) matching the
search/filtering criteria. Supported filters are the same as for the
`/catalog/v2/entries`_ endpoint.


``/catch/external``
-------------------

===== ===========
Type: :ref:`private <private-api-endpoint>`
===== ===========

**Usage:**

  ``/catch/external?source=URL``

Generates a HTML page with a link leading to (the decoded version of) ``URL``
and a warning that following that link will load an external (out of ZIM)
resource.

**Parameters:**

  ``source``: URL of the external resource (must be URL-encoded).

**Example:**

.. code:: sh

  # Intercept an external link to https://example.com?query=abcd
  $ curl 'http://localhost:8080/catch/external?source=https%3A%2F%2Fexample.com%3Fquery%3Dabcd'



``/content``
------------

===== ===========
Type: :ref:`private <private-api-endpoint>`
===== ===========

ZIM file content is served under the ``/content`` endpoint as described below.


``/content/ZIMNAME/PATH/IN/ZIMFILE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: :ref:`private <private-api-endpoint>`
===== ===========

Returns the entry with path ``PATH/IN/ZIMFILE`` from ZIM file with :term:`name
<ZIM name>` ``ZIMNAME``.


``/content/ZIMNAME``
^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: :ref:`private <private-api-endpoint>`
===== ===========

``/content/ZIMNAME`` redirects to the main page of the ZIM file with :term:`name
<ZIM name>` ``ZIMNAME`` (unless that ZIM file contains an entry with an empty
path or path equal to ``/``, in which case that entry is returned).


``/random``
-----------

===== ===========
Type: :ref:`private <private-api-endpoint>`
===== ===========

**Usage:**

  ``/random?content=ZIMNAME``

Generates a HTTP redirect to a randomly selected article/page from the
specified ZIM file.

**Parameters:**

  ``content``: :term:`name of the ZIM file <ZIM name>`.


.. _raw:

``/raw``
--------

===== ===========
Type: :ref:`public <public-api-endpoint>`
===== ===========

The ``/raw`` API provides access to ZIM file data. It consists of two separate
endpoints for accessing data and metadata.


``/raw/ZIMNAME/content/PATH/IN/ZIMFILE``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: member of a :ref:`public API <raw>`
===== ===========

Returns the entry with path ``PATH/IN/ZIMFILE`` from the ZIM file with
:term:`name <ZIM name>` ``ZIMNAME``. Currently, this endpoint almost duplicates
(with some subtle technical differences) the newer endpoint
`/content/ZIMNAME/PATH/IN/ZIMFILE`_. The important difference is that the
``/raw`` endpoint guarantees that no server-side processing will be applied to
the returned content, whereas content obtained via the ``/content`` endpoint
may in the future undergo some processing intended to improve the operation of
the viewer (e.g. compensating for certain bugs in ZIM creation). Also note that
``/raw`` is :ref:`public <public-api-endpoint>`, whereas ``/content`` is
:ref:`private <private-api-endpoint>`.


``/raw/ZIMNAME/meta/METADATAID``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

===== ===========
Type: member of a :ref:`public API <raw>`
===== ===========

Returns the metadata item ``METADATAID`` from the ZIM file with :term:`name
<ZIM name>` ``ZIMNAME``.


``/search``
-----------

===== ===========
Type: :ref:`public <public-api-endpoint>`
===== ===========

Performs a full text search on one or more ZIM files and returns an HTML page
with a list of links to matching pages along with snippets of the matching
portions of those pages.

.. _multi-zim-search-constraints:

A multi-ZIM search request must comply with the following constraints:

* the number of ZIM files participating in the search operation must not exceed
  the limit imposed by the :option:`--searchLimit` option of ``kiwix-serve``.

* all of the ZIM files participating in the same search operation must be in
  the same language.

**Parameters:**


  ZIM file selection parameters:

    At least one of the following parameters must be provided in order to
    specify in which ZIM file(s) to search. Parameters appearing earlier in
    below list take precedence over subsequent ones (the later ones, even if
    present in the request, are simply ignored).

    ``content``: :term:`name of the ZIM file <ZIM name>` (for a single-ZIM
    search). This is a :ref:`legacy parameter <deprecation>`. ``books.name``
    should be used instead.

    ``books.id``: :term:`UUID <ZIM UUID>` of the ZIM file. Can be repeated for
    a multi-ZIM search, however must respect the :ref:`multi-ZIM search
    constraints <multi-zim-search-constraints>`.

      .. note::

        If any of the provided ``books.id`` values refers to a book missing
        from the library then an error is returned instead of running the
        search on the remaining (valid) entries.

    ``books.name``: :term:`name of the ZIM file <ZIM name>` (not to be confused
    with ``books.filter.name`` which selects/filters based on the :term:`book
    name <Book name>`). Can be repeated for a multi-ZIM search, however must
    respect the :ref:`multi-ZIM search constraints
    <multi-zim-search-constraints>`.

      .. note::

        If any of the provided ``books.name`` values refers to a book missing
        from the library then an error is returned instead of running the
        search on the remaining (valid) entries.

    ``books.filter.{criteria}``: allows to take full advantage of :ref:`library
    filtering <library-filtering>` functionality of the `/catalog/v2/entries`_
    endpoint (``{criteria}`` must be replaced with an attribute/filtering
    criteria name supported by :ref:`library filtering <library-filtering>`).

  Query parameters:

    ``pattern`` (optional; defaults to an empty string): text to search for.

    ``latitude``, ``longitude`` & ``distance`` (optional): geospatial query
    parameters. If all of these are provided, then the results will be
    restricted to geotagged pages that are within ``distance`` metres from the
    location on Earth with coordinates ``latitude`` and ``longitude``.

  Pagination parameters:

    ``pageLength`` (optional, default: 25): maximum number of search results in
    the response. Capped at 140.

    ``start`` (optional, default: 0): this parameter enables pagination of
    results. The response will include up to ``pageLength`` results starting
    with entry # ``start`` from the full list of search results (the first
    result is assumed to have index 0).

  Other parameters:

    ``format`` (optional, default: html): format of the search results. Allowed
    values are: html, xml.

Examples:

.. code:: sh

  # Search for 'android' in the book with name 'scifi-library'
  # Return results ## 51-60.
  $ curl 'http://localhost:8080/search?pattern=android&books.name=scifi-library&start=51&pageLength=10'

  # Search for 'napoli' in books in Italian
  $ curl 'http://localhost:8080/search?books.filter.lang=ita&pattern=napoli'

  # Search for 'chateau' in books in French that have a category of 'wikipedia'.
  # Return the results as XML.
  $ curl 'http://localhost:8080/search?pattern=chateau&books.filter.lang=fra&books.filter.category=wikipedia&format=xml'


``/search/searchdescription.xml``
---------------------------------

===== ===========
Type: :ref:`public <public-api-endpoint>`
===== ===========

Describes the `/search`_ endpoint in `OpenSearch description format
<https://developer.mozilla.org/en-US/docs/Web/OpenSearch>`_.



``/skin``
-----------

===== ===========
Type: :ref:`private <private-api-endpoint>`
===== ===========

Static front-end resources (such as CSS, javascript and images) are all grouped
under ``/skin``.

**Usage:**
  ``/skin/PATH/TO/RESOURCE[?cacheid=CACHEID]``

`Cache busting
<https://javascript.plainenglish.io/what-is-cache-busting-55366b3ac022>`_ of
static resources is supported via the optional param ``cacheid``. By default,
i.e. when the ``cacheid`` parameter is not specified while accessing the
``/skin`` endpoint, static resources are served as if they were dynamic (i.e.
could be different for an immediately repeated request). Specifying the
``cacheid`` parameter with a correct value (matching the value embedded in the
``kiwix-serve`` instance), makes the returned resource to be presented as
immutable. However, if the value of the ``cacheid`` parameter mismatches then
``kiwix-serve`` responds with a 404 HTTP error.

``kiwix-serve``'s default front-end (the :ref:`welcome page <welcome-page>` and
the :ref:`ZIM file viewer <zim-file-viewer>`) access all underlying static
resources by using explicit ``cacheid`` s.


``/suggest``
------------

===== ===========
Type: :ref:`private <private-api-endpoint>`
===== ===========

**Usage:**

  ``/suggest?content=ZIMNAME[&term=QUERY][&count=N][&start=S]``

Returns suggestions (in JSON format) for a text string that is assumed to be a
partially typed search for a page inside a particular ZIM file.

Suggestions are obtained as matches of the query text against the page titles
in the ZIM file using the title index database generated during the creation of
the ZIM file.

In case of a multi-word query the order of the words matters in two ways:

1. the last word is considered as partially typed, unless followed by a space;
2. ranking of the matches.

If the ZIM file doesn't contain a title index then suggestions are generated by
listing page titles starting *exactly* (in a case sensitive manner) with the
query text. Otherwise, suggestions are case-insensitive.

If the ZIM file contains a full text search index, then an extra suggestion is
added as an option to perform a full text search in the said ZIM file.

**Parameters:**

  ``content`` (mandatory): :term:`name of the ZIM file <ZIM name>`.

  ``term`` (optional; defaults to an empty string): query text.

  ``count`` (optional, default: 10): maximum number of page suggestions in the
  response (i.e. the extra option to perform a full text search is not included
  in this count).

  ``start`` (optional, default: 0): this parameter enables pagination of
  results. The response will include up to ``count`` entries starting with
  entry # ``start`` from the full list of page suggestions (the first result is
  assumed to have index 0).

**Example:**

.. code:: sh

  $ curl 'http://localhost/suggest?content=stackoverflow_en&term=pyth&count=50'


.. _zim-file-viewer:

``/viewer``
-----------

===== ===========
Type: :ref:`private <private-api-endpoint>`
===== ===========

ZIM file viewer. The ZIM file and entry therein must be specified via the hash
component of the URL as ``/viewer#ZIMNAME/PATH/IN/ZIMFILE``.


``/viewer_settings.js``
-----------------------

===== ===========
Type: :ref:`private <private-api-endpoint>`
===== ===========

Settings of the ZIM file viewer that are configurable via certain command line
options of ``kiwix-serve`` (e.g. ``--nolibrarybutton``).


/ANYTHING/ELSE
--------------

===== ===========
Type: :ref:`private <private-api-endpoint>`
===== ===========

Any other URL is considered as an attempt to access ZIM file content using the
legacy URL scheme and is redirected to ``/content/ANYTHING/ELSE``.


Glossary
========

.. glossary::

  Book name

    Name of the book as specified in the ZIM file metadata (for a
    ``kiwix-serve`` started *WITHOUT* the :option:`--library` option) or the
    library XML file (for a ``kiwix-serve`` started with the
    :option:`--library` option).

    .. note::

      Two or more books may have the same name in the library. That's not
      considered a conflict, because there may be multiple versions of the
      "same" book (differing by the settings of the scraper, date, etc).
      :ref:`Library filtering <library-filtering>` by name will return all
      matching books.

  ZIM filename

    Name of a ZIM file on the server filesystem.

  ZIM name

    Identifier of a ZIM file in the server's library (used for referring to a
    particular ZIM file in requests).

    ZIM names are derived from the filenames as follows:

    - file extension is removed,
    - all characters are converted to lowercase,
    - diacritics are removed,
    - spaces are replaced with underscores,
    - ``+`` symbols are replaced with the text ``plus``.

    Presence of the :option:`-z`/:option:`--nodatealiases` option will create
    additional names (aliases) for filenames with dates.

    ZIM names are expected to be unique across the library. Any name conflicts
    (including those caused by the usage of the
    :option:`-z`/:option:`--nodatealiases` option) are reported on STDERR but,
    otherwise, are ignored (i.e. only one of the entries can be accessed via
    the conflicting name).

  ZIM title

    Title of a ZIM file. This can be any text (with whitespace). It is never
    used as a way of referring to a ZIM file.

  ZIM UUID

    This is a unique identifier of a ZIM file designated at its creation time
    and embedded in the ZIM file. Certain ``kiwix-serve`` operations may
    require that a ZIM file be referenced through its UUID rather than name.



================================================
FILE: docs/meson.build
================================================

sphinx = find_program('sphinx-build', native:true)

sphinx_target = run_target('doc',
    command: [sphinx, '-bhtml',
              meson.current_source_dir(),
              meson.current_build_dir()])



================================================
FILE: docs/requirements.txt
================================================
Sphinx==5.3.0
sphinx-rtd-theme==1.1.1



================================================
FILE: src/meson.build
================================================
subdir('manager')
subdir('searcher')
subdir('server')
subdir('man')



================================================
FILE: src/version.h
================================================
/*
 * Copyright 2009-2016 Emmanuel Engelhart <kelson@kiwix.org>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 */

#ifndef _KIWIX_TOOLS_VERSION_H_
#define _KIWIX_TOOLS_VERSION_H_

#ifndef KIWIX_TOOLS_VERSION
  #define KIWIX_TOOLS_VERSION "undefined"
#endif

#include <kiwix/version.h>
#include <zim/version.h>
#include <iostream>

void version()
{
  std::cout << "kiwix-tools " << KIWIX_TOOLS_VERSION << std::endl << std::endl;
  kiwix::printVersions();
  std::cout << std::endl;
  zim::printVersions();
}

#endif //_KIWIX_TOOLs_VERSION_H_



================================================
FILE: src/man/kiwix-manage.1
================================================
.TH KIWIX-MANAGE 1 "21 May 2012"

.SH NAME
kiwix\-manage \- Kiwix Library Manager

.SH SYNOPSIS
.IX Header SYNOPSIS
.TP
\fBkiwix\-manage\fR LIBRARY_PATH \fBadd\fR ZIM_PATH ...
.TP
\fBkiwix\-manage\fR LIBRARY_PATH \fBshow\fR [ZIM_ID_1] [ZIM_ID_2] ...
.TP
\fBkiwix\-manage\fR LIBRARY_PATH \fBremove\fR ZIM_ID_1 [ZIM_ID_2] ...
.TP
\fBkiwix\-manage\fR --version
.TP
\fBkiwix\-manage\fR --help

.SH DESCRIPTION
.PP
\fBkiwix\-manage\fP is a command line tool for manipulating a Kiwix XML library.
.PP
\fBkiwix\-manage\fP allows to manage the entries of the Kiwix
library. The library file is a flat XML file listing ZIM files with
all necessary information like id, favicon, date, creator,
description, filepath, title, url, etc.

.SH ACTIONS

.TP
\fBadd\fR
Add \fBZIM_FILE\fP to \fBLIBRARY_FILE\fP. Create the library file if necessary.

.TP
\fBremove\fR
Remove the given \fBZIM_ID\fR from \fBLIBRARY_FILE\fR. At least one \fBZIM_ID\fR should be specified.

.TP
\fBshow\fR
Show given \fBZIM_ID\fP from \fBLIBRARY_FILE\fR. If no \fBZIM_ID\fP is given then all contents from \fBLIBRARY_FILE\fR are shown.

.SH OPTIONS
.TP
Options to be used with the action \fBadd\fR:

.TP
\fB\-\-url=HTTP_URL\fR
Set the ZIM online HTTP(S) URL

.TP
\fB\-\-zimPathToSave=OTHER_FS_PATH\fR
Set an arbitrary ZIM filesystem path (instead of the ZIM_PATH)

.TP
Other options (to be used alone):

.TP
\fB\-\-help | \-h\fR
Display the kiwix-manage help

.TP
\fB\-\-version | \-v\fR
Display the version of kiwix-manage and all dependences

.SH SEE ALSO
kiwix\-serve(1)

.SH AUTHORS
Kiwix team <contact@kiwix.org>



================================================
FILE: src/man/kiwix-search.1
================================================
.TH KIWIX-SEARCH "1" "July 2020" "kiwix-tools" "User Commands"
.SH NAME
kiwix-search \- find articles using a fulltext search pattern
.SH SYNOPSIS
\fBkiwix-search\fR [OPTIONS] ZIM PATTERN\fR
.SH DESCRIPTION
.TP
ZIM
ZIM file to search
.TP
PATTERN
Words or parts of words to search for in the ZIM file
.TP
\fB\-s\fR, \fB\-\-suggestion\fR
Suggest article titles based on the PATTERN instead of a fulltext search
.TP
\fB\-V\fR, \fB\-\-version\fR
print software version
.TP
\fB\-v\fR, \fB\-\-verbose\fR
Give details about the search process



================================================
FILE: src/man/kiwix-serve.1
================================================
.TH KIWIX 1 "10 July 2023"

.SH NAME
kiwix-serve \- Kiwix HTTP Server

.SH SYNOPSIS

.B kiwix-serve --library [OPTIONS] LIBRARY_FILE_PATH
.br
.B kiwix-serve [OPTIONS] ZIM_FILE_PATH ...

.SH DESCRIPTION
The \fBkiwix-serve\fR command is used to run a stand-alone HTTP server for serving ZIM contents over the network.

.SH ARGUMENTS
.TP
\fBLIBRARY_FILE_PATH\fR
Path of an XML library file listing ZIM files to serve. To be used only with the --library option. Multiple library files can be provided as a semicolon (;) separated list.

.TP
\fBZIM_FILE_PATH ...\fR
ZIM file path(s). Multiple arguments are allowed.

.SH OPTIONS
.TP
\fB--library\fR
By default, kiwix-serve expects a list of ZIM files as command line arguments. Providing the --library option tells kiwix-serve that the command line argument is rather a library XML file.

.TP
\fB-i ADDR, --address=ADDR\fR
Listen only on this IP address. By default, the server listens on all available IP addresses. Alternatively, you can use special values to define which types of connections to accept:

all : Listen for connections on all IP addresses (IPv4 and IPv6).
.br
ipv4 : Listen for connections on all IPv4 addresses.
.br
ipv6 : Listen for connections on all IPv6 addresses.

.TP
\fB-p PORT, --port=PORT\fR
TCP port on which to listen for HTTP requests (default: 80).

.TP
\fB-r ROOT, --urlRootLocation=ROOT\fR
URL prefix on which the content should be made available (default: empty).

.TP
\fB-d, --daemon\fR
Detach the HTTP server daemon from the main process.

.TP
\fB-a PID, --attachToProcess=PID\fR
Exit when the process with id PID stops running.

.TP
\fB-M, --monitorLibrary\fR
Monitor the XML library file and reload it automatically when it changes.

Library reloading can be forced anytime by sending a SIGHUP signal to the
\*(lqkiwix-serve\*(rq process (this works regardless of the presence of the
\*(lq--monitorLibrary\*(rq/\*(lq-M\*(rq option).

.TP
\fB-m, --nolibrarybutton\fR
Disable the library home button in the ZIM viewer toolbar.

.TP
\fB-n, --nosearchbar\fR
Disable the search box in the ZIM viewer toolbar.

.TP
\fB-b, --blockexternal\fR
Prevent users from directly navigating to external resources via links in ZIM content.

.TP
\fB-t N, --threads=N\fR
Number of threads to run in parallel (default: 4).

.TP
\fB-s N, --searchLimit=N\fR
Maximum number of ZIM files in a fulltext multizim search (default: No limit).

.TP
\fB-z, --nodatealiases\fR
Create URL aliases for each content by removing the date embedded in the file name.

The expected format of the date in the filename is \*(lq_YYYY-MM\*(rq. For example, a ZIM file named \*(lqwikipedia_en_all_2020-08.zim\*(rq will be accessible both as \*(lqwikipedia_en_all_2020-08\*(rq and \*(lqwikipedia_en_all\*(rq.

.TP
\fB-c PATH, --customIndex=PATH\fR
Override the welcome page with a custom HTML file.

.TP
\fB-L N, --ipConnectionLimit=N\fR
Max number of (concurrent) connections per IP (default: infinite, recommended: >= 6).

.TP
\fB-k, --skipInvalid\fR
Startup even when ZIM files are invalid (those will be skipped)

.TP
\fB-v, --verbose\fR
Print debug log to STDOUT.

.TP
\fB-V, --version\fR
Print the software version.

.TP
\fB-h, --help\fR
Print a help message.

.SH EXAMPLES
Serve a single ZIM file:
.sp
.nf
.B kiwix-serve myzim.zim
.fi

Serve multiple ZIM files:
.sp
.nf
.B kiwix-serve zim1.zim zim2.zim zim3.zim
.fi

Serve ZIM files from a library:
.sp
.nf
.B kiwix-serve --library library.xml
.fi

.SH DOCUMENTATION
Online documentation: https://kiwix-tools.readthedocs.io/en/latest/kiwix-serve.html
.br
Source code: https://github.com/kiwix/kiwix-tools
.br
More info: https://wiki.kiwix.org/wiki/Kiwix-serve

.SH AUTHORS
Emmanuel Engelhart <kelson@kiwix.org>
.br
Vasudev Kamath <kamathvasudev@gmail.com>



================================================
FILE: src/man/meson.build
================================================
install_man('kiwix-manage.1',
            'kiwix-search.1',
            'kiwix-serve.1')
subdir('fr')



================================================
FILE: src/man/fr/kiwix-manage.1
================================================
.TH KIWIX 1 "21 May 2012"
.SH NAME
kiwix\-manage \- Gestionnaire de bibliothèque Kiwix
.SH SYNOPSIS
.IX Header SYNOPSIS
.B kiwix\-manage
.br
kiwix\-manage LIBRARY_PATH add ZIM_PATH ...
.br
	kiwix-manage LIBRARY_PATH show [CONTENTID1] [CONTENTID2] ...
.br
	kiwix\-manage LIBRARY_PATH remove CONTENTID1 [CONTENTID2]
.SH DESCRIPTION
.SS kiwix\-manage

.PP
Permet de gérer les contenus de la bibliothèque Kiwix. La bibliothèque est un fichier
XML référencant les contenus ZIM et leurs méta-donnnées: Index, icone, date, etc.

.
.PP
Un fichier d'exemple est disponible à http://www.kiwix.org/library\.xml

.TP
\fBadd\fR
Ajoute le fichier \fBZIM_FILE\fP à la bibliothèque \fBLIBRARY_FILE\fP.

.TP
\fBshow\fR
Show given \fBCONTENT_ID\fP from \fBLIBRARY_FILE\fR. If no \fBCONTENT_ID\fP is given then all contents from \fBLIBRARY_FILE\fR are shown.
Affiche les détails de \fBCONTENT_ID\fP dans la bibliothèque \fBLIBRARY_FILE\fR.
.br
Sans \fBCONTENT_ID\fP, tous les contenus sont affichés.

.TP
\fBremove\fR
Supprime le contenu \fBCONTENT_ID\fR de la bibliothèque. Au moins un \fBCONTENT_ID\fR doit être spécifié.

.TP
\fB\-\-zimPathToSave=\fR
Change le chemin de référence du fichier ZIM dans la bibliothèque.

.TP
\fB\-\-current\fR
Marque ce contenu comme celui courant (contenu par défaut) dans la biliothèque.

.TP
\fB\-\-backend=xapian|clucene\fR
Séléctionne un moteur d'indexation.

.TP
\fB\-\-indexPath=FULLTEXT_IDX_PATH\fR
Chemin vers l'index plein texte correspondant au fichier ZIM.

.TP
\fBurl\fR
Définit l'adresse URL corresponsant au fichier ZIM pour pouvoir être téléchargé depuis Kiwix.

.SH SEE ALSO
kiwix(1) kiwix\-install(1) kiwix\-serve(1)
.SH AUTHOR
Emmanuel Engelhart <kelson@kiwix.org>
.br
Vasudev Kamath <kamathvasudev@gmail.com> (Manual)



================================================
FILE: src/man/fr/kiwix-serve.1
================================================
.TH KIWIX 1 "21 May 2012"
.SH NAME
kiwix\-serve \- Serveur Web Kiwix
.SH SYNOPSIS
.IX Header "SYNOPSIS"
.br
kiwix\-serve [\-\-index=INDEX_PATH] [\-\-port=PORT] [\-\-verbose] [\-\-daemon] [\-\-attachToProcess=PID] ZIM_PATH
.br
kiwix\-serve \-\-library [\-\-port=PORT] [\-\-verbose] [\-\-daemon] [\-\-attachToProcess=PID] LIBRARY_PATH
.SH DESCRIPTION
.PP
Serveur Web (HTTP) autonome pour diffuser des contenus ZIM sur le réseau.

.TP
\fB\-\-index=INDEX_PATH\fR
Chemin vers l'index plein text du fichier ZIM.

.TP
\fB\-\-port=PORT\fR
Port sur lequel le serveur doit écouter.
.br
Par défaut, le serveur écoute sur le port 80.

.TP
\fB\-\-verbose\fR
Active le mode verbeux de la sortie.

.TP
\fB\-\-daemon\fR
Execute le serveur en mode démon.

.TP
\fB\-\-attachToProcess=PID\fR
Arrêter le serveur lorsque que le processus PID meurt.

.TP
\fBZIM_PATH\fR
Chemin vers le fichier ZIM à diffuser.
.br
Obligatoire en dehors du mode bibliothèque.

.TP
\fB\-\-library\fR
Active le mode bibliothèque.
.br
Sert les contenus d'une bibliothèque Kiwix au lieu d'un seul fichier ZIM.

.TP
\fBLIBRARY_PATH\fR
Chemin vers le fichier bibliothèque de Kiwix.
.br
Le fichier bibliothèque est un fichier XML créé avec \fBkiwix-manage\fB.

.SH SEE ALSO
kiwix(1) kiwix\-manage(1)
.br
kiwix\-install(1)
.SH AUTHOR
Emmanuel Engelhart <kelson@kiwix.org>
.br
Vasudev Kamath <kamathvasudev@gmail.com> (Manual)



================================================
FILE: src/man/fr/meson.build
================================================
install_man('kiwix-manage.1',
            'kiwix-serve.1',
            install_dir:get_option('mandir')+'/fr/man1')



================================================
FILE: src/manager/kiwix-manage.cpp
================================================
/*
 * Copyright 2011-2019 Emmanuel Engelhart <kelson@kiwix.org>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU  General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 */

#include <docopt/docopt.h>
#include <kiwix/manager.h>
#include <kiwix/tools.h>
#include <cstdlib>
#include <iostream>

#include "../version.h"

using namespace std;

enum supportedAction { NONE, ADD, SHOW, REMOVE };

void show(const kiwix::Library& library, const std::string& bookId)
{
  try {
    auto& book = library.getBookById(bookId);
    std::cout << "id:\t\t" << book.getId() << std::endl
              << "path:\t\t" << book.getPath() << std::endl
              << "url:\t\t" << book.getUrl() << std::endl
              << "title:\t\t" << book.getTitle() << std::endl
              << "name:\t\t" << book.getName() << std::endl
              << "tags:\t\t" << book.getTags() << std::endl
              << "description:\t" << book.getDescription() << std::endl
              << "creator:\t" << book.getCreator() << std::endl
              << "date:\t\t" << book.getDate() << std::endl
              << "articleCount:\t" << book.getArticleCount() << std::endl
              << "mediaCount:\t" << book.getMediaCount() << std::endl
              << "size:\t\t" << book.getSize() << " KB" << std::endl;
  } catch (std::out_of_range&) {
     std::cout << "No book " << bookId << " in the library" << std::endl;
  }
  std::cout << std::endl;
}

// Older version of docopt doesn't declare Options. Let's declare it ourself.
using Options = std::map<std::string, docopt::value>;


/* Print correct console usage options */
static const char USAGE[] =
R"(Manipulates the Kiwix library XML file

Usage:
 kiwix-manage LIBRARYPATH add [--zimPathToSave=<custom_zim_path>] [--url=<http_zim_url>] ZIMPATH ...
 kiwix-manage LIBRARYPATH (delete|remove) ZIMID ...
 kiwix-manage LIBRARYPATH show [ZIMID ...]
 kiwix-manage -v | --version
 kiwix-manage -h | --help

Arguments:
  LIBRARYPATH    The XML library file path.
  ZIMID          ZIM file unique ID.
  ZIMPATH        A path to a ZIM to add.

Options:
  Custom options for "add" action:
    --zimPathToSave=<custom_zim_path>  Replace the current ZIM file path
    --url=<http_zim_url>               Create an "url" attribute for the online version of the ZIM file

  Other options:
    -h --help                          Print this help
    -v --version                       Print the software version

Examples:
 Add ZIM files to library:       kiwix-manage my_library.xml add first.zim second.zim
 Remove ZIM files from library:  kiwix-manage my_library.xml remove e5c2c003-b49e-2756-5176-5d9c86393dd9
 Show all library ZIM files:     kiwix-manage my_library.xml show

Documentation:
  Source code  https://github.com/kiwix/kiwix-tools
  More info    https://wiki.kiwix.org/wiki/kiwix-manage
)";

int handle_show(const kiwix::Library& library, const std::string& libraryPath,
                 const Options& options)
{
  if (options.at("ZIMID").asStringList().empty()) {
    auto booksIds = library.getBooksIds();
    for(auto& bookId: booksIds) {
      show(library, bookId);
    }
  } else {
    auto bookIds = options.at("ZIMID").asStringList();
    for(auto& bookId: bookIds) {
       show(library, bookId);
    }
  }

  return(0);
}

int handle_add(kiwix::LibraryPtr library, const std::string& libraryPath,
                const Options& options)
{
  string zimPathToSave;
  string url;

  kiwix::Manager manager(library);

  auto zimPaths = options.at("ZIMPATH").asStringList();
  for (auto& zimPath: zimPaths) {
    if (options.at("--zimPathToSave").isString()) {
      zimPathToSave = options.at("--zimPathToSave").asString();
    } else {
      zimPathToSave = zimPath;
    }
    if (options.at("--url").isString()) {
      url = options.at("--url").asString();
    }

    if (manager.addBookFromPathAndGetId(zimPath, zimPathToSave, url, false).empty()) {
      std::cerr << "Cannot add ZIM " << zimPath << " to the library." << std::endl;
      return 1;
    }
  }

  return 0;
}

int handle_remove(kiwix::Library& library, const std::string& libraryPath,
                   const Options& options)
{
  const unsigned int totalBookCount = library.getBookCount(true, true);
  int exitCode = 0;

  if (!totalBookCount) {
    std::cerr << "Library is empty, no book to delete."
              << std::endl;
    return 1;
  }

  auto bookIds = options.at("ZIMID").asStringList();
  for (auto& bookId: bookIds) {
    if (!library.removeBookById(bookId)) {
      std::cerr << "Invalid book id '" << bookId << "'." << std::endl;
      exitCode = 1;
    }
  }

  return(exitCode);
}

int main(int argc, char** argv)
{
  supportedAction action = NONE;
  auto library = kiwix::Library::create();

  Options args;
  try {
    args = docopt::docopt_parse(USAGE, {argv+1, argv+argc}, false, false);
  } catch (docopt::DocoptArgumentError const & error ) {
    std::cerr << error.what() << std::endl;
    std::cerr << USAGE << std::endl;
    return -1;
  }

  if (args["--help"].asBool()) {
    std::cout << USAGE << std::endl;
    return 0;
  }

  if (args["--version"].asBool()) {
    version();
    return 0;
  }

  std::string libraryPath = args.at("LIBRARYPATH").asString();

  if (args.at("add").asBool())
    action = ADD;
  else if (args.at("show").asBool())
    action = SHOW;
  else if (args.at("remove").asBool() || args.at("delete").asBool())
    action = REMOVE;

  /* Try to read the file */
  libraryPath = kiwix::isRelativePath(libraryPath)
                    ? kiwix::computeAbsolutePath(kiwix::getCurrentDirectory(), libraryPath)
                    : libraryPath;
  kiwix::Manager manager(library);
  if (!manager.readFile(libraryPath, false)) {
    if (kiwix::fileExists(libraryPath) || action!=ADD) {
      std::cerr << "Cannot read the library " << libraryPath << std::endl;
      return 1;
    }
  }

  /* SHOW */
  int exitCode = 0;
  switch (action) {
    case SHOW:
      exitCode = handle_show(*library, libraryPath, args);
      break;
    case ADD:
      exitCode = handle_add(library, libraryPath, args);
      break;
    case REMOVE:
      exitCode = handle_remove(*library, libraryPath, args);
      break;
    case NONE:
      break;
  }

  if (exitCode) {
    return exitCode;
  }

  /* Rewrite the library file */
  if (action == REMOVE || action == ADD) {
    // writeToFile return true (1) if everything is ok => exitCode is 0
    if (!library->writeToFile(libraryPath)) {
      std::cerr << "Cannot write the library " << libraryPath << std::endl;
      return 1;
    }
  }

  return 0;
}



================================================
FILE: src/manager/meson.build
================================================
executable('kiwix-manage', ['kiwix-manage.cpp'],
  dependencies:all_deps,
  install:true)



================================================
FILE: src/searcher/kiwix-search.cpp
================================================
/*
 * Copyright 2011 Emmanuel Engelhart <kelson@kiwix.org>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU  General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 */

#include <docopt/docopt.h>

#include <zim/search.h>
#include <zim/suggestion.h>

#include <kiwix/spelling_correction.h>
#include <xapian.h>

#include <iostream>
#include <filesystem>

#include "../version.h"

using namespace std;


// Older version of docopt doesn't declare Options. Let's declare it ourself.
using Options = std::map<std::string, docopt::value>;

static const char USAGE[] =
R"(Find articles based on a fulltext search pattern.

Usage:
  kiwix-search [options] ZIM PATTERN
  kiwix-search -h | --help
  kiwix-search -V | --version

Arguments:
  ZIM       The full path of the ZIM file
  PATTERN   Word(s) - or part of - to search in the ZIM.

Options:
  -s --suggestion    Suggest article titles based on the few letters of the PATTERN instead of making a fulltext search. Work a bit like a completion solution
  --spelling         Suggest article titles based on the spelling corrected PATTERN instead of making a fulltext search.
  -v --verbose       Give details about the search process
  -V --version       Print software version
  -h --help          Print this help
)";

std::filesystem::path getKiwixCachedDataDirPath()
{
  std::filesystem::path home(getenv("HOME"));
  std::filesystem::path cacheDirPath = home / ".cache" / "kiwix";
  std::filesystem::create_directories(cacheDirPath);
  return cacheDirPath;
}

int main(int argc, char** argv)
{
  Options args;
  try {
    args = docopt::docopt_parse(USAGE, {argv+1, argv+argc}, false, false);
  } catch (docopt::DocoptArgumentError const & error ) {
    std::cerr << error.what() << std::endl;
    std::cerr << USAGE << std::endl;
    return -1;
  }

  if (args.at("--help").asBool()) {
    std::cout << USAGE << std::endl;
    return 0;
  }

  if (args.at("--version").asBool()) {
    version();
    return 0;
  }

  auto zimPath = args.at("ZIM").asString();
  auto pattern = args.at("PATTERN").asString();
  auto verboseFlag = args.at("--verbose").asBool();

  /* Try to prepare the indexing */
  try {
    zim::Archive archive(zimPath);

    if (args.at("--suggestion").asBool()) {
      zim::SuggestionSearcher searcher(archive);
      searcher.setVerbose(verboseFlag);
      for (const auto& r:searcher.suggest(pattern).getResults(0, 10)) {
        cout << r.getTitle() << endl;
      }
    }  else if (args.at("--spelling").asBool()) {
      kiwix::SpellingsDB spellingsDB(archive, getKiwixCachedDataDirPath());
      for (const auto& r:spellingsDB.getSpellingCorrections(pattern, 1)) {
        cout << r << endl;
      }
    } else {
      zim::Searcher searcher(archive);
      searcher.setVerbose(verboseFlag);
      const zim::Query query(pattern);
      for (const auto& r : searcher.search(query).getResults(0, 10) ) {
        cout << r.getTitle() << endl;
      }
    }
  } catch ( const std::runtime_error& err)  {
    cerr << err.what() << endl;
    exit(1);
  } catch ( const Xapian::Error& err)  {
    cerr << err.get_msg() << endl;
    exit(1);
  }

  exit(0);
}



================================================
FILE: src/searcher/meson.build
================================================
executable('kiwix-search', ['kiwix-search.cpp'],
  dependencies:all_deps,
  install:true)



================================================
FILE: src/server/kiwix-serve.cpp
================================================

/*
 * Copyright 2009-2019 Emmanuel Engelhart <kelson@kiwix.org>
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU  General Public License as published by
 * the Free Software Foundation; either version 3 of the License, or
 * any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
 * MA 02110-1301, USA.
 */

#include <docopt/docopt.h>
#include <kiwix/manager.h>
#include <kiwix/server.h>
#include <kiwix/name_mapper.h>
#include <kiwix/tools.h>

#ifdef _WIN32
# include <windows.h>
#else
# include <unistd.h>
# include <signal.h>
#endif
#include <sys/stat.h>

#ifdef __APPLE__
# import <sys/sysctl.h>
# import <sys/types.h>
# define MIBSIZE 4
#endif

#include "../version.h"

#define DEFAULT_THREADS 4
#define LITERAL_AS_STR(A) #A
#define AS_STR(A) LITERAL_AS_STR(A)


static const char USAGE[] =
R"(Deliver ZIM file(s) articles via HTTP

Usage:
 kiwix-serve [options] ZIMPATH ...
 kiwix-serve [options] (-l | --library) LIBRARYPATH
 kiwix-serve -h | --help
 kiwix-serve -V | --version

Mandatory arguments:
  LIBRARYPATH  XML library file path listing ZIM file to serve. To be used only with the --library argument."
  ZIMPATH      ZIM file path(s)

Options:
 -h --help                               Print this help
 -a <pid> --attachToProcess=<pid>        Exit if given process id is not running anymore [default: 0]
 --catalogOnly                           Serve only the library catalog
 --contentServerURL=<url>                Root URL of the server serving ZIM content for this library
 -d --daemon                             Detach the HTTP server daemon from the main process
 -i <address> --address=<address>        Listen only on the specified IP address. Specify 'ipv4', 'ipv6' or 'all' to listen on all IPv4, IPv6 or both types of addresses, respectively [default: all]
 -M --monitorLibrary                     Monitor the XML library file and reload it automatically
 -m --nolibrarybutton                    Don't print the builtin home button in the builtin top bar overlay
 -n --nosearchbar                        Don't print the builtin bar overlay on the top of each served page
 -b --blockexternal                      Prevent users from directly accessing external links
 -p <port> --port=<port>                 Port on which to listen to HTTP requests [default: 80]
 -r <root> --urlRootLocation=<root>      URL prefix on which the content should be made available [default: /]
 -s <limit> --searchLimit=<limit>        Maximun number of zim in a fulltext multizim search [default: 0]
 -t <threads> --threads=<threads>        Number of threads to run in parallel [default: )" AS_STR(DEFAULT_THREADS) R"(]
 -v --verbose                            Print debug log to STDOUT
 -V --version                            Print software version
 -z --nodatealiases                      Create URL aliases for each content by removing the date
 -c <path> --customIndex=<path>          Add path to custom index.html for welcome page
 -L <limit> --ipConnectionLimit=<limit>  Max number of (concurrent) connections per IP [default: 0] (recommended: >= 6)
 -k --skipInvalid                        Startup even when ZIM files are invalid (those will be skipped)

Documentation:
  Source code   https://github.com/kiwix/kiwix-tools
  More info     https://wiki.kiwix.org/wiki/Kiwix-serve
                https://kiwix-tools.readthedocs.io/en/latest/kiwix-serve.html
)";

std::string loadCustomTemplate (std::string customIndexPath) {
  customIndexPath = kiwix::isRelativePath(customIndexPath) ?
                      kiwix::computeAbsolutePath(kiwix::getCurrentDirectory(), customIndexPath) :
                      customIndexPath;
  if (!kiwix::fileReadable(customIndexPath)) {
    throw std::runtime_error("No such file exist (or file is not readable) " + customIndexPath);
  }
  if (kiwix::getMimeTypeForFile(customIndexPath) != "text/html") {
    throw std::runtime_error("Invalid File Mime Type " + kiwix::getMimeTypeForFile(customIndexPath));
  }
  std::string indexTemplateString = kiwix::getFileContent(customIndexPath);

  if (indexTemplateString.empty()) {
    throw std::runtime_error("Unreadable or empty file " + customIndexPath);
  }
  return indexTemplateString;
}

#ifndef _WIN32
volatile sig_atomic_t waiting = false;
volatile sig_atomic_t libraryMustBeReloaded = false;
void handle_sigterm(int signum)
{
    if ( waiting == false ) {
        _exit(signum);
    }
    waiting = false;
}

void handle_sighup(int signum)
{
  libraryMustBeReloaded = true;
}

typedef void (*SignalHandler)(int);

void set_signal_handler(int sig, SignalHandler handler)
{
    struct sigaction sa;
    sigaction(sig, NULL, &sa);
    sa.sa_handler = handler;
    sigaction(sig, &sa, NULL);
}

void setup_sighandlers()
{
    set_signal_handler(SIGTERM, &handle_sigterm);
    set_signal_handler(SIGINT,  &handle_sigterm);
    set_signal_handler(SIGHUP,  &handle_sighup);
}
#else
bool waiting = false;
bool libraryMustBeReloaded = false;
#endif

uint64_t fileModificationTime(const std::string& path)
{
#if defined(_WIN32) && !defined(stat)
#define stat _stat
#endif
  struct stat fileStatData;
  if ( stat(path.c_str(), &fileStatData) == 0 ) {
    return fileStatData.st_mtime;
  }
  return 0;
#ifdef _WIN32
#undef stat
#endif
}

uint64_t newestFileTimestamp(const std::vector<std::string>& paths)
{
  uint64_t t = 0;
  for ( const auto& p : paths ) {
    t = std::max(t, fileModificationTime(p));
  }

  return t;
}

bool reloadLibrary(kiwix::Manager& mgr, const std::vector<std::string>& paths)
{
    try {
      std::cout << "Loading the library from the following files:\n";
      for ( const auto& p : paths ) {
        std::cout << "\t" << p << std::endl;
      }
      mgr.reload(paths);
      std::cout << "The library was successfully loaded." << std::endl;
      return true;
    } catch ( const std::runtime_error& err ) {
      std::cerr << "ERROR: " << err.what() << std::endl;
      std::cerr << "Errors encountered while loading the library." << std::endl;
      return false;
    }
}

// docopt::value::isLong() is counting repeated values.
// It doesn't check if the string can be parsed as long.
// (Contrarly to `asLong` which will try to convert string to long)
// See https://github.com/docopt/docopt.cpp/issues/62
// `isLong` is a small helper to get if the value can be parsed as long.
inline bool isLong(const docopt::value& v) {
  try {
    v.asLong();
    return true;
  } catch (...) {
    return false;
  }
}

#define FLAG(NAME, VAR) if (arg.first == NAME) { VAR = arg.second.asBool(); continue; }
#define STRING(NAME, VAR) if (arg.first == NAME && arg.second.isString() ) { VAR = arg.second.asString(); continue; }
#define STRING_LIST(NAME, VAR, ERRORSTR) if (arg.first == NAME) { if (arg.second.isStringList()) { VAR = arg.second.asStringList(); continue; } else { errorString = ERRORSTR; break; } }
#define INT(NAME, VAR, ERRORSTR) if (arg.first == NAME ) { if (isLong(arg.second)) { VAR = arg.second.asLong(); continue; } else { errorString = ERRORSTR; break; } }

// Older version of docopt doesn't declare Options. Let's declare it ourself.
using Options = std::map<std::string, docopt::value>;

int main(int argc, char** argv)
{
#ifndef _WIN32
  setup_sighandlers();
#endif

  std::string rootLocation = "/";
  auto library = kiwix::Library::create();
  unsigned int nb_threads = DEFAULT_THREADS;
  std::vector<std::string> zimPathes;
  std::string libraryPath;
  std::string rootPath;
  std::string address;
  std::string customIndexPath="";
  std::string indexTemplateString="";
  int serverPort = 80;
  bool catalogOnlyFlag = false;
  std::string contentServerURL;
  bool daemonFlag [[gnu::unused]] = false;
  bool helpFlag = false;
  bool noLibraryButtonFlag = false;
  bool noSearchBarFlag = false;
  bool noDateAliasesFlag = false;
  bool blockExternalLinks = false;
  bool isVerboseFlag = false;
  bool monitorLibrary = false;
  bool versionFlag = false;
  unsigned int PPID = 0;
  int ipConnectionLimit = 0;
  int searchLimit = 0;
  bool skipInvalid = false;

  std::string errorString;

  Options args;
  try {
    args = docopt::docopt_parse(USAGE, {argv+1, argv+argc}, false, false);
  } catch (docopt::DocoptArgumentError const & error) {
    std::cerr << error.what() << std::endl;
    std::cerr << USAGE << std::endl;
    return -1;
  }

  for (auto const& arg: args) {
    FLAG("--help", helpFlag)
    FLAG("--catalogOnly", catalogOnlyFlag)
    STRING("--contentServerURL", contentServerURL)
    FLAG("--daemon", daemonFlag)
    FLAG("--verbose", isVerboseFlag)
    FLAG("--nosearchbar", noSearchBarFlag)
    FLAG("--blockexternal", blockExternalLinks)
    FLAG("--nodatealiases", noDateAliasesFlag)
    FLAG("--nolibrarybutton",noLibraryButtonFlag)
    FLAG("--monitorLibrary", monitorLibrary)
    FLAG("--skipInvalid", skipInvalid)
    FLAG("--version", versionFlag)
    STRING("LIBRARYPATH", libraryPath)
    INT("--port", serverPort, "Port must be an integer")
    INT("--attachToProcess", PPID, "Process to attach must be an integer")
    STRING("--address", address)
    INT("--threads", nb_threads, "Number of threads must be an integer")
    STRING("--urlRootLocation", rootLocation)
    STRING("--customIndex", customIndexPath)
    INT("--ipConnectionLimit", ipConnectionLimit, "IP connection limit must be an integer")
    INT("--searchLimit", searchLimit, "Search limit must be an integer")
    STRING_LIST("ZIMPATH", zimPathes, "ZIMPATH must be a string list")
 }

 if (!errorString.empty()) {
   std::cerr << errorString << std::endl;
   std::cerr << USAGE << std::endl;
   return -1;
 }

 if (helpFlag) {
   std::cout << USAGE << std::endl;
   return 0;
 }

 if (versionFlag) {
   version();
   return 0;
 }

  /* Setup the library manager and get the list of books */
  kiwix::Manager manager(library);
  std::vector<std::string> libraryPaths;
  if (!libraryPath.empty()) {
    libraryPaths = kiwix::split(libraryPath, ";");
    if ( !reloadLibrary(manager, libraryPaths) ) {
      exit(1);
    }

    /* Check if the library is not empty (or only remote books)*/
    if (library->getBookCount(true, false) == 0) {
      std::cerr << "The XML library file '" << libraryPath
           << "' is empty (or has only remote books)." << std::endl;
    }
  } else {
    std::vector<std::string>::iterator it;
    for (it = zimPathes.begin(); it != zimPathes.end(); it++) {
      if (!manager.addBookFromPath(*it, *it, "", false)) {
        if (skipInvalid) {
          std::cerr << "Skipping invalid '" << *it << "' ...continuing" << std::endl;
        } else {
          std::cerr << "Unable to add the ZIM file '" << *it
               << "' to the internal library." << std::endl;
          exit(1);
        }
      }
    }
  }
  auto libraryFileTimestamp = newestFileTimestamp(libraryPaths);
  auto curLibraryFileTimestamp = libraryFileTimestamp;

  kiwix::IpMode ipMode = kiwix::IpMode::AUTO;

  if (address == "all") {
    address.clear();
    ipMode = kiwix::IpMode::ALL;
  } else if (address == "ipv4") {
    address.clear();
    ipMode = kiwix::IpMode::IPV4;
  } else if (address == "ipv6") {
    address.clear();
    ipMode = kiwix::IpMode::IPV6;
  }

#ifndef _WIN32
  /* Fork if necessary */
  if (daemonFlag) {
    pid_t pid;

    /* Fork off the parent process */
    pid = fork();
    if (pid < 0) {
      exit(1);
    }

    /* If we got a good PID, then
       we can exit the parent process. */
    if (pid > 0) {
      exit(0);
    }
  }
#endif

  auto nameMapper = std::make_shared<kiwix::UpdatableNameMapper>(library, noDateAliasesFlag);
  kiwix::Server server(library, nameMapper);

  if (!customIndexPath.empty()) {
    try {
      indexTemplateString = loadCustomTemplate(customIndexPath);
    } catch (std::runtime_error& e) {
      std::cerr << "ERROR: " << e.what() << std::endl;
      exit(1);
    }
  }

  server.setAddress(address);
  server.setRoot(rootLocation);
  server.setPort(serverPort);
  server.setNbThreads(nb_threads);
  server.setVerbose(isVerboseFlag);
  server.setTaskbar(!noSearchBarFlag, !noLibraryButtonFlag);
  server.setBlockExternalLinks(blockExternalLinks);
  server.setIndexTemplateString(indexTemplateString);
  server.setIpConnectionLimit(ipConnectionLimit);
  server.setMultiZimSearchLimit(searchLimit);
  server.setIpMode(ipMode);
  server.setCatalogOnlyMode(catalogOnlyFlag);
  while ( !contentServerURL.empty() && contentServerURL.back() == '/' )
    contentServerURL.pop_back();
  server.setContentServerUrl(contentServerURL);

  if (! server.start()) {
    exit(1);
  }
  
  std::cout << "The Kiwix server is running and can be accessed in the local network at: " << std::endl;
  for (const auto& url : server.getServerAccessUrls()) {
    std::cout << "  - " << url << std::endl;
  }

  /* Run endless (until PPID dies) */
  waiting = true;
  do {
    if (PPID > 0) {
#ifdef _WIN32
      HANDLE process = OpenProcess(SYNCHRONIZE, FALSE, PPID);
      DWORD ret = WaitForSingleObject(process, 0);
      CloseHandle(process);
      if (ret == WAIT_TIMEOUT) {
#elif __APPLE__
      int mib[MIBSIZE];
      struct kinfo_proc kp;
      size_t len = sizeof(kp);

      mib[0] = CTL_KERN;
      mib[1] = KERN_PROC;
      mib[2] = KERN_PROC_PID;
      mib[3] = PPID;

      int ret = sysctl(mib, MIBSIZE, &kp, &len, NULL, 0);
      if (ret != -1 && len > 0) {
#else /* Linux & co */
      std::string procPath = "/proc/" + std::to_string(PPID);
      if (access(procPath.c_str(), F_OK) != -1) {
#endif
      } else {
        waiting = false;
      }
    }

    kiwix::sleep(1000);

    if ( monitorLibrary ) {
      curLibraryFileTimestamp = newestFileTimestamp(libraryPaths);
      if ( !libraryMustBeReloaded ) {
        libraryMustBeReloaded = curLibraryFileTimestamp > libraryFileTimestamp;
      }
    }

    if ( libraryMustBeReloaded && !libraryPaths.empty() ) {
      libraryFileTimestamp = curLibraryFileTimestamp;
      reloadLibrary(manager, libraryPaths);
      nameMapper->update();
      libraryMustBeReloaded = false;
    }
  } while (waiting);

  /* Stop the daemon */
  server.stop();
}



================================================
FILE: src/server/meson.build
================================================

sources = ['kiwix-serve.cpp']

executable('kiwix-serve', sources,
  dependencies:all_deps,
  install:true)



================================================
FILE: .github/FUNDING.yml
================================================
# These are supported funding model platforms

github: kiwix # Replace with up to 4 GitHub Sponsors-enabled usernames e.g., [user1, user2]
patreon: # Replace with a single Patreon username
open_collective: # Replace with a single Open Collective username
ko_fi: # Replace with a single Ko-fi username
tidelift: # Replace with a single Tidelift platform-name/package-name e.g., npm/babel
community_bridge: # Replace with a single Community Bridge project-name e.g., cloud-foundry
liberapay: # Replace with a single Liberapay username
issuehunt: # Replace with a single IssueHunt username
otechie: # Replace with a single Otechie username
custom: # https://kiwix.org/support-us/



================================================
FILE: .github/move.yml
================================================
# Configuration for Move Issues - https://github.com/dessant/move-issues

# Delete the command comment when it contains no other content
deleteCommand: true

# Close the source issue after moving
closeSourceIssue: true

# Lock the source issue after moving
lockSourceIssue: false

# Mention issue and comment authors
mentionAuthors: true

# Preserve mentions in the issue content
keepContentMentions: true

# Move labels that also exist on the target repository
moveLabels: true

# Set custom aliases for targets
# aliases:
#   r: repo
#   or: owner/repo

# Repository to extend settings from
# _extends: repo


================================================
FILE: .github/workflows/ci.yml
================================================
name: CI

on:
  pull_request:
  push:
    branches:
      - main

jobs:
  Windows:
    runs-on: windows-2025

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python 3.10
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install packages
        run:
          choco install pkgconfiglite ninja

      - name: Install python modules
        run: pip3 install meson

      - name: Setup MSVC compiler
        uses: bus1/cabuild/action/msdevshell@v1
        with:
          architecture: x64

      - name: Install dependencies
        uses: kiwix/kiwix-build/actions/dl_deps_archive@main
        with:
          target_platform: win-x86_64-static

      - name: Compile
        shell: cmd
        run: |
          set PKG_CONFIG_PATH=%cd%\BUILD_win-amd64\INSTALL\lib\pkgconfig
          set CPPFLAGS=-I%cd%\BUILD_win-amd64\INSTALL\include
          meson.exe setup . build -Dstatic-linkage=true --buildtype=release
          cd build
          ninja.exe

      - name: Test
        shell: cmd
        run: |
          cd build
          meson.exe test --verbose
        env:
          WAIT_TIME_FACTOR_TEST: 10

  Linux:
    runs-on: ubuntu-22.04

    strategy:
      fail-fast: false
      matrix:
        target:
          - linux-x86_64-static
          - linux-x86_64-dyn
        include:
          - target: linux-x86_64-static
            image_variant: jammy
            lib_postfix: '/x86_64-linux-gnu'
            arch_name: linux-x86_64
          - target: linux-x86_64-dyn
            image_variant: jammy
            lib_postfix: '/x86_64-linux-gnu'
            arch_name: linux-x86_64

    env:
      HOME: /home/runner

    container:
      image: "ghcr.io/kiwix/kiwix-build_ci_${{matrix.image_variant}}:2025-06-07"

    steps:
    - name: Checkout code
      uses: actions/checkout@v4

    - name: Install dependencies
      uses: kiwix/kiwix-build/actions/dl_deps_archive@main
      with:
        target_platform: ${{ matrix.target }}

    - name: Compile
      shell: bash
      run: |
        if [[ "${{matrix.target}}" =~ .*-static ]]; then
          MESON_OPTION="-Dstatic-linkage=true"
        else
          MESON_OPTION=""
        fi
        if [ -e "$HOME/BUILD_${{matrix.arch_name}}/meson_cross_file.txt" ]; then
          MESON_OPTION="$MESON_OPTION --cross-file $HOME/BUILD_${{matrix.arch_name}}/meson_cross_file.txt"
        fi
        meson . build ${MESON_OPTION}
        cd build
        ninja
      env:
        PKG_CONFIG_PATH: "${{env.HOME}}/BUILD_${{matrix.arch_name}}/INSTALL/lib/pkgconfig:${{env.HOME}}/BUILD_${{matrix.arch_name}}/INSTALL/lib${{matrix.lib_postfix}}/pkgconfig"
        CPPFLAGS: "-I${{env.HOME}}/BUILD_${{matrix.arch_name}}/INSTALL/include"



================================================
FILE: .github/workflows/docker.yml
================================================
name: Docker

on:
  workflow_dispatch:
    inputs:
      version:
        description: Specific version to build (overrides on-master and tag-pattern)
        required: false
        default: ''

jobs:
  build-and-push-kiwix-tools:
    name: Deploy kiwix-tools Docker Image
    runs-on: ubuntu-22.04
    steps:
      - uses: actions/checkout@v4
      - name: build and publish kiwix-tools
        uses: openzim/docker-publish-action@v10
        with:
          image-name: kiwix/kiwix-tools
          registries: ghcr.io
          credentials: |
            GHCRIO_USERNAME=${{ secrets.GHCR_USERNAME }}
            GHCRIO_TOKEN=${{ secrets.GHCR_TOKEN }}
          context: docker
          latest-on-tag: true
          build-args:
            VERSION={tag}
          platforms: |
            linux/amd64
            linux/arm64
            linux/arm/v7
            linux/arm/v6
            linux/386
          restrict-to: kiwix/kiwix-tools
          manual-tag: ${{ github.event.inputs.version }}
          repo_description: auto
          repo_overview: Kiwix command line tools

  build-and-push-kiwix-serve:
    name: Deploy kiwix-serve Docker Image
    runs-on: ubuntu-22.04
    needs: build-and-push-kiwix-tools
    steps:
      - uses: actions/checkout@v4
      - name: build and publish kiwix-serve
        uses: openzim/docker-publish-action@v10
        with:
          image-name: kiwix/kiwix-serve
          registries: ghcr.io
          credentials: |
            GHCRIO_USERNAME=${{ secrets.GHCR_USERNAME }}
            GHCRIO_TOKEN=${{ secrets.GHCR_TOKEN }}
          context: docker/server
          latest-on-tag: true
          build-args:
            VERSION={tag}
          platforms: |
            linux/amd64
            linux/arm64
            linux/arm/v7
            linux/arm/v6
            linux/386
          restrict-to: kiwix/kiwix-tools
          manual-tag: ${{ github.event.inputs.version }}
          repo_description: auto
          repo_overview: Kiwix web-server



================================================
FILE: .github/workflows/package.yml
================================================
name: Packages
on:
  pull_request:
  push:
    branches:
      - main
  release:
    types: [published]

jobs:
  build-deb:
    runs-on: ubuntu-22.04
    strategy:
      fail-fast: false
      matrix:
        distro:
#          - debian-unstable
#          - debian-trixie
#          - debian-bookworm
#          - debian-bullseye
          - ubuntu-noble
          - ubuntu-jammy

    steps:
      - uses: actions/checkout@v4

      # Determine which PPA we should upload to
      - name: PPA
        id: ppa
        run: |
          if [[ $REF == refs/tags* ]]
          then
            echo "ppa=kiwixteam/release" >> $GITHUB_OUTPUT
          else
            echo "ppa=kiwixteam/dev" >> $GITHUB_OUTPUT
          fi
        env:
          REF: ${{ github.ref }}

      - uses: legoktm/gh-action-auto-dch@main
        with:
          fullname: Kiwix builder
          email: release+launchpad@kiwix.org
          distro: ${{ matrix.distro }}

#      - uses: legoktm/gh-action-build-deb@debian-unstable
#        if: matrix.distro == 'debian-unstable'
#        name: Build package for debian-unstable
#        id: build-debian-unstable
#        with:
#          args: --no-sign
#
#      - uses: legoktm/gh-action-build-deb@b47978ba8498dc8b8153cc3b5f99a5fc1afa5de1 # pin@debian-trixie
#        if: matrix.distro == 'debian-trixie'
#        name: Build package for debian-trixie
#        id: build-debian-trixie
#        with:
#          args: --no-sign
#
#      - uses: legoktm/gh-action-build-deb@1f4e86a6bb34aaad388167eaf5eb85d553935336 # pin@debian-bookworm
#        if: matrix.distro == 'debian-bookworm'
#        name: Build package for debian-bookworm
#        id: build-debian-bookworm
#        with:
#          args: --no-sign
#
#      - uses: legoktm/gh-action-build-deb@084b4263209252ec80a75d2c78a586192c17f18d # pin@debian-bullseye
#        if: matrix.distro == 'debian-bullseye'
#        name: Build package for debian-bullseye
#        id: build-debian-bullseye
#        with:
#          args: --no-sign

      - uses: legoktm/gh-action-build-deb@9114a536498b65c40b932209b9833aa942bf108d # pin@ubuntu-noble
        if: matrix.distro == 'ubuntu-noble'
        name: Build package for ubuntu-noble
        id: build-ubuntu-noble
        with:
          args: --no-sign
          ppa: ${{ steps.ppa.outputs.ppa }}

      - uses: legoktm/gh-action-build-deb@ubuntu-jammy
        if: matrix.distro == 'ubuntu-jammy'
        name: Build package for ubuntu-jammy
        id: build-ubuntu-jammy
        with:
          args: --no-sign
          ppa: ${{ steps.ppa.outputs.ppa }}

      - uses: actions/upload-artifact@v4
        with:
          name: Packages for ${{ matrix.distro }}
          path: output

      - uses: legoktm/gh-action-dput@main
        name: Upload dev package
        # Only upload on pushes to git default branch
        if: github.event_name == 'push' && github.event.ref == 'refs/heads/main' && startswith(matrix.distro, 'ubuntu-')
        with:
          gpg_key: ${{ secrets.LAUNCHPAD_GPG }}
          repository: ppa:kiwixteam/dev
          packages: output/*_source.changes

      - uses: legoktm/gh-action-dput@main
        name: Upload release package
        if: github.event_name == 'release' && startswith(matrix.distro, 'ubuntu-')
        with:
          gpg_key: ${{ secrets.LAUNCHPAD_GPG }}
          repository: ppa:kiwixteam/release
          packages: output/*_source.changes



================================================
FILE: .well-known/funding-manifest-urls
================================================
https://kiwix.org/funding.json



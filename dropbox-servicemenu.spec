Name:           dropbox-servicemenu
Version:        0.16.1
Release:        1%{?dist}
Summary:        Dropbox servicemenu for Konqueror and Dolphin

Group:          Applications/Internet
License:        GPLv3+
URL:            http://kde-apps.org/content/show.php/Dropbox+ServiceMenu?content=124416
Source0:        http://kde-apps.org/CONTENT/content-files/124416-DropboxServiceMenu-%{version}.tar.gz

BuildArch:      noarch

BuildRequires:  kdebase
BuildRequires:  desktop-file-utils

Requires:       kdebase
Requires:       python-crypto
Requires:       xdg-utils
Requires:       recode
Requires:       perl


%description
Dropbox ServiceMenu is a servicemenu which allows easy access to most
of Dropbox features.
dropbox must be installed for proper work.

%prep
%setup -q -n DropboxServiceMenu-%{version}
#Correct paths
sed 's|=`kde4-config --localprefix`/share/kde4/services/ServiceMenus/dropbox-scripts/dropbox_menu.sh|=dropbox_menu.sh|g' -i dropbox*.desktop
sed 's|SCRIPTS_PATH="`kde4-config --localprefix`share/kde4/services/ServiceMenus/dropbox-scripts/"|SCRIPTS_PATH=/usr/bin/|g' -i dropbox-scripts/dropbox_menu.sh
#Adding shebang
sed -i "1i #!/bin/bash" dropbox-scripts/dropbox_menu_translations.sh

%build
# nothing to build


%install
mkdir -p %{buildroot}%{_kde4_sharedir}/kde4/services/ServiceMenus/
mkdir -p %{buildroot}%{_bindir}

install -m 755 dropbox-scripts/get_dropbox_folder.sh %{buildroot}%{_bindir}/get_dropbox_folder.sh
install -m 755 dropbox-scripts/pyndexer.py %{buildroot}%{_bindir}/pyndexer.py
install -m 755 dropbox-scripts/dropbox.py %{buildroot}%{_bindir}/dropbox.py
install -m 755 dropbox-scripts/dropbox-notify.py %{buildroot}%{_bindir}/dropbox-notify.py
install -m 755 dropbox-scripts/dropbox_menu.sh %{buildroot}%{_bindir}/dropbox_menu.sh
install -m 755 dropbox-scripts/dropbox_menu_translations.sh %{buildroot}%{_bindir}/dropbox_menu_translations.sh

install -m 644 dropbox_all.desktop %{buildroot}%{_kde4_sharedir}/kde4/services/ServiceMenus/
install -m 644 dropbox_directories.desktop %{buildroot}%{_kde4_sharedir}/kde4/services/ServiceMenus/
install -m 644 dropbox_files.desktop %{buildroot}%{_kde4_sharedir}/kde4/services/ServiceMenus/



%files
%doc LICENSE Changelog THANKS
%{_bindir}/pyndexer.py
%{_bindir}/get_dropbox_folder.sh
%{_bindir}/dropbox.py
%{_bindir}/dropbox-notify.py
%{_bindir}/dropbox_menu.sh
%{_bindir}/dropbox_menu_translations.sh
%{_kde4_sharedir}/kde4/services/ServiceMenus/dropbox_all.desktop
%{_kde4_sharedir}/kde4/services/ServiceMenus/dropbox_directories.desktop
%{_kde4_sharedir}/kde4/services/ServiceMenus/dropbox_files.desktop


%changelog
* Thu May 16 2013 Vasiliy N. Glazov <vascom2@gmail.com> - 0.16.1-1
- update to 0.16.1
- clean spec

* Fri Feb 11 2011 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.15.3-1
- version bump

* Fri Dec 03 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.15.1-1
- version bump

* Sun Sep 26 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.14.5-1
- version bump

* Fri Jul 09 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.14.4-1
- version bump

* Fri Jul 09 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.14.3-1
- version bump

* Wed Jun 30 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.14.2-1
- version bump

* Mon Jun 28 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.14.1-1
- version bump

* Sun Jun 27 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.14.0-2
- fix version tag

* Sat Jun 26 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.14.0-1
- version bump

* Sun Jun 13 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.13.5-1
- version bump

* Wed Jun 09 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.13.3-1
- version bump

* Wed Jun 09 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.13.2-1
- version bump

* Mon Jun 07 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.13.1-1
- version bump

* Mon Jun 07 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.12.2-1
- version bump

* Mon Jun 07 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.11.1-1
- version bump

* Sun Jun 06 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.11.0-1
- version bump
- add Requires python-crypto, new feature
- add THANKS doc

* Mon Jun 04 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.10.0-1
- version bump

* Mon May 31 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.9.1-1
- version bump

* Sun May 30 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.9.0-1
- version bump

* Sat May 29 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.8.4-1
- version bump

* Wed May 19 2010 Magnus Tuominen <magnus.tuominen@gmail.com> - 0.8.2-1
- first build

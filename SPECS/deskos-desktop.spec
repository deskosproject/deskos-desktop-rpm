Name:           deskos-desktop
Version:        0.3.0
Release:        1%{?dist}
Summary:        DeskOS Desktop dependencies

Group:          System Utilities
License:        GPLv3+
URL:            https://deskosproject.org
BuildArch:      noarch

Requires:       deskos-backgrounds
Requires:       deskos-firefox-preferences
Requires:       deskos-firefox-theme
Requires:       deskos-gnome-theme
Requires:       deskos-icon-theme
Requires:       deskos-indexhtml
Requires:       deskos-logos
Requires:       deskos-multimedia-codecs
Requires:       deskos-settings-gnome
Requires:       firefox-extension-htitle
Requires:       freetype-freeworld
Requires:       gnome-shell-theme-deskos
Requires:       plymouth-theme-deskos
Requires:       thunderbird-es-configuration

%description
DeskOS Desktop dependencies.

%files

%changelog
* Tue Dec 20 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.3.0-1
- Added deskos-firefox-theme and firefox-extension-htitle

* Fri Nov 18 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.2.0-1
- Added deskos-multimedia-codecs

* Fri Sep 16 2016 Ricardo Arguello <rarguello@deskosproject.org> - 0.1.0-1
- Initial release

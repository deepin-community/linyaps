%global debug_package %{nil}
Name:           linglong
Version:        1.4.3
Release:        1
Summary:        Linglong Package FrameWork
License:        LGPLv3
URL:            https://github.com/linuxdeepin/%{name}
Source0:        %{url}/archive/%{version}/linglong-%{version}.tar

BuildRequires:  cmake gcc-c++
BuildRequires:  qt5-qtbase-devel qt5-qtbase-private-devel
BuildRequires:  glib2-devel nlohmann-json-devel ostree-devel yaml-cpp-devel
BuildRequires:  systemd-devel gtest-devel elfutils-libelf-devel
BuildRequires:  glibc-static libstdc++-static
BuildRequires:  libcurl-devel openssl-devel
BuildRequires:  gtest-devel gmock-devel erofs-utils
BuildRequires:  libcap-devel gettext-devel
BuildRequires:  libuuid-devel
Requires:       linglong-bin = %{version}-%{release}

%description
This package is a linglong package framework.

%package        -n linglong-bin
Summary:        Linglong package manager
Requires:       linglong-box
Requires:       pkexec erofs-utils
Recommends:     erofsfuse
%description    -n linglong-bin
Linglong package management command line tool.

%package        -n linglong-builder
Summary:        Linglong build tools
Requires:       linglong-box linglong-bin = %{version}-%{release}
Requires:       erofs-utils fuse-overlayfs uidmap
Recommends:     git
%description    -n linglong-builder
This package is a tool that makes it easy to build applications and dependencies.

%prep
%autosetup -p1 -n linglong-%{version}

%define _debugsource_template %{nil}

%build
export PATH=%{_qt5_bindir}:$PATH
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
      -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
      -DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
      -DLIB_INSTALL_DIR:PATH=%{_libdir} \
      -DSYSCONF_INSTALL_DIR:PATH=%{_sysconfdir} \
      -DSHARE_INSTALL_PREFIX:PATH=%{_datadir} \
      -DBUILD_SHARED_LIBS=OFF \
      -DCPM_LOCAL_PACKAGES_ONLY=ON ..
%make_build

%install
cd build
%make_install INSTALL_ROOT=%{buildroot}

%post -n linglong-bin
%systemd_post org.deepin.linglong.PackageManager.service

%preun -n linglong-bin
%systemd_preun org.deepin.linglong.PackageManager.service

%postun -n linglong-bin
%systemd_postun_with_restart org.deepin.linglong.PackageManager.service

%files
%doc README.md
%license LICENSE
%exclude %{_libdir}/cmake/linglong-*/*.cmake

%files -n linglong-bin
%doc README.md
%license LICENSE
%{_sysconfdir}/profile.d/*
%{_sysconfdir}/X11/Xsession.d/*
%{_bindir}/ll-cli
%{_bindir}/llpkg
%{_prefix}/lib/%{name}/container/*
%{_prefix}/lib/%{name}/generate-xdg-data-dirs.sh
%{_prefix}/lib/sysusers.d/*.conf
%{_prefix}/lib/tmpfiles.d/*.conf
%{_prefix}/lib/systemd/system/*.service
%{_prefix}/lib/systemd/system-preset/*.preset
%{_prefix}/lib/systemd/user/*
%{_prefix}/lib/systemd/system-environment-generators/*
%{_prefix}/lib/systemd/user-generators/*
%{_libexecdir}/%{name}/ll-package-manager
%{_libexecdir}/%{name}/ll-session-helper
%{_libexecdir}/%{name}/ld-cache-generator
%{_libexecdir}/%{name}/font-cache-generator
%{_libexecdir}/%{name}/ll-dialog
%{_libexecdir}/%{name}/ll-init
%{_libexecdir}/%{name}/ll-driver-detect
%{_libexecdir}/%{name}/dialog/99-linglong-permission
%{_datadir}/bash-completion/completions/ll-cli
%{_datadir}/zsh/vendor-completions/_ll-cli
%{_datadir}/dbus-1/system-services/*.service
%{_datadir}/dbus-1/system.d/*.conf
%{_datadir}/polkit-1/actions/org.deepin.linglong.PackageManager1.policy
%{_datadir}/%{name}/config.yaml
%{_datadir}/%{name}/export-dirs.json
%{_datadir}/mime/packages/*
%{_datadir}/locale/*
%{_datadir}/applications/*
%{_datadir}/icons/*

%files -n linglong-builder
%license LICENSE
%{_bindir}/ll-builder
%{_libexecdir}/%{name}/fetch-dsc-source
%{_libexecdir}/%{name}/fetch-git-source
%{_libexecdir}/%{name}/fetch-file-source
%{_libexecdir}/%{name}/fetch-archive-source
%{_libexecdir}/%{name}/app-conf-generator
%{_libexecdir}/%{name}/builder/helper/*.sh
%{_datadir}/bash-completion/completions/ll-builder
%{_datadir}/%{name}/builder/templates/*.yaml
%{_datadir}/%{name}/builder/uab/*

%changelog
* Thu Apr 25 2024 chenhuixing <chenhuixing@deepin.org> - 1.4.3-1
- Init project

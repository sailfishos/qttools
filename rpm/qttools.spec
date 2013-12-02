%define keep_static 1
Name:       qt5-qttools
Summary:    Development tools for Qt
Version:    5.0.2
Release:    1%{?dist}
Group:      Qt/Qt
License:    LGPLv2.1 with exception or GPLv3
URL:        http://qt.nokia.com
Source:     %{name}-%{version}.tar.bz2
BuildRequires:  qt5-qtgui-devel
BuildRequires:  qt5-qtnetwork-devel
BuildRequires:  qt5-qtcore-devel
BuildRequires:  qt5-qtsql-devel
BuildRequires:  qt5-qtxml-devel
BuildRequires:  qt5-qtwidgets-devel
BuildRequires:  qt5-qtprintsupport-devel
BuildRequires:  qt5-qtplatformsupport-devel
BuildRequires:  qt5-qtbootstrap-devel
BuildRequires:  qt5-qmake
BuildRequires:  qt5-tools
BuildRequires:  qt5-qtdbus-devel
BuildRequires:  pkgconfig(Qt5QmlDevTools)
BuildRequires:  fdupes

%description
Qt is a cross-platform application and UI framework. Using Qt, you can
write web-enabled applications once and deploy them across desktop,
mobile and embedded systems without rewriting the source code.
.
This package contains additional tools for building Qt applications.

%package linguist
Summary:    The linguist tools
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description linguist
This package contains the linguist tool

%package pixeltool
Summary:    The pixeltool tool
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description pixeltool
This package contains the pixeltool tool

%package kmap2qmap
Summary:    The kmap2qmap tool
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description kmap2qmap
This package contains the kmap2qmap tool

%package qdbus
Summary:    The qdbus and qdbusviewer tool
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qdbus
This package contains the qdbus and qdbusviewer tool

%package paths
Summary:    Command line client for standard paths
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}

%description paths
This package contains the qtpaths tool.

%package qtuitools
Summary:    The QtUiTools library
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtuitools
This package contains the QtUiTools library

%package qtuitools-devel
Summary:    Development files for QtUiTools
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
 
%description qtuitools-devel
This package contains the files necessary to develop
applications that use QtUiTools


%package qtclucene
Summary:    The QtCLucene library
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qtclucene
This package contains the QtCLucene library

%package qtclucene-devel
Summary:    Development files for QtLucense
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
 
%description qtclucene-devel
This package contains the files necessary to develop
applications that use QtCLucene

%package qtdesigner
Summary: The Qt designer libraries
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%package qthelp
Summary:    The QtHelp library
Group:      Qt/Qt
Requires:   %{name} = %{version}-%{release}
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig

%description qthelp
This package contains the QtHelp library

%package qthelp-devel
Summary:    Development files for QtHelp
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
 
%description qthelp-devel
This package contains the files necessary to develop
applications that use QtHelp

%description qtdesigner
This package contains the files necessary to develop
applications that use QtDesigner

%package qtdesigner-devel
Summary:    Development files for QtDesigner
Group:      Qt/Qt
Requires(post):     /sbin/ldconfig
Requires(postun):   /sbin/ldconfig
 
%description qtdesigner-devel
This package contains the files necessary to develop
applications that use QtDesigner



%prep
%setup -q -n %{name}-%{version}

%build
export QTDIR=/usr/share/qt5
touch .git
%qmake5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
%qmake5_install

# Remove unneeded .la files
rm -f %{buildroot}/%{_libdir}/*.la

# We don't need qt5/Qt/
rm -rf %{buildroot}/%{_includedir}/qt5/Qt

# Fix wrong path in pkgconfig files
find %{buildroot}%{_libdir}/pkgconfig -type f -name '*.pc' \
-exec perl -pi -e "s, -L%{_builddir}/?\S+,,g" {} \;
# Fix wrong path in prl files
find %{buildroot}%{_libdir} -type f -name '*.prl' \
-exec sed -i -e "/^QMAKE_PRL_BUILD_DIR/d;s/\(QMAKE_PRL_LIBS =\).*/\1/" {} \;

%fdupes %{buildroot}/%{_libdir}
%fdupes %{buildroot}/%{_includedir}
%fdupes %{buildroot}/%{_datadir}


%post
/sbin/ldconfig
%postun
/sbin/ldconfig

%post qtuitools -p /sbin/ldconfig
%postun qtuitools -p /sbin/ldconfig

%post qthelp -p /sbin/ldconfig
%postun qthelp -p /sbin/ldconfig

%post qtclucene -p /sbin/ldconfig
%postun qtclucene -p /sbin/ldconfig

%post qtdesigner -p /sbin/ldconfig
%postun qtdesigner -p /sbin/ldconfig



%files
%defattr(-,root,root,-)

%files linguist
%defattr(-,root,root,-)
%{_qt5_bindir}/lconvert
%{_qt5_bindir}/linguist
%{_qt5_bindir}/lrelease
%{_qt5_bindir}/lupdate
%{_datadir}/qt5/phrasebooks/
%{_libdir}/cmake/Qt5Linguist*

%files pixeltool
%defattr(-,root,root,-)
%{_qt5_bindir}/pixeltool

%files kmap2qmap
%defattr(-,root,root,-)
%{_qt5_bindir}/kmap2qmap

%files qdbus
%defattr(-,root,root,-)
%{_qt5_bindir}/qdbus
%{_qt5_bindir}/qdbusviewer

%files paths
%defattr(-,root,root,-)
%{_qt5_bindir}/qtpaths

%files qtuitools
%defattr(-,root,root,-)

%files qtuitools-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtUiTools/
%{_libdir}/libQt5UiTools.prl
%{_libdir}/libQt5UiTools.a
%{_libdir}/pkgconfig/Qt5UiTools.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_uitools.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_uitools_private.pri
%{_libdir}/cmake/Qt5UiTools/

%files qthelp
%defattr(-,root,root,-)
%{_libdir}/libQt5Help.so.*

%files qthelp-devel
%defattr(-,root,root,-)
%{_qt5_bindir}/assistant
%{_qt5_bindir}/qhelpgenerator
%{_qt5_bindir}/qcollectiongenerator
%{_qt5_bindir}/qhelpconverter
%{_includedir}/qt5/QtHelp/
%{_libdir}/libQt5Help.prl
%{_libdir}/libQt5Help.so
%{_libdir}/pkgconfig/Qt5Help.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_help.pri
%{_datadir}/qt5/mkspecs/modules/qt_lib_help_private.pri
%{_libdir}/cmake/Qt5Help/

%files qtclucene
%defattr(-,root,root,-)
%{_libdir}/libQt5CLucene.so.*

%files qtclucene-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtCLucene/
%{_libdir}/libQt5CLucene.prl
%{_libdir}/libQt5CLucene.so
%{_libdir}/pkgconfig/Qt5CLucene.pc
%{_datadir}/qt5/mkspecs/modules/qt_lib_clucene_private.pri

%files qtdesigner
%defattr(-,root,root,-)
%{_qt5_bindir}/designer
%{_libdir}/libQt5Designer*.so.*

%files qtdesigner-devel
%defattr(-,root,root,-)
%{_includedir}/qt5/QtDesigner/
%{_includedir}/qt5/QtDesignerComponents/
%{_libdir}/libQt5Designer*.so
%{_libdir}/libQt5Designer*.prl
%{_datadir}/qt5/mkspecs/modules/qt_lib_designer*.pri
%{_libdir}/pkgconfig/Qt5Designer*.pc
%{_libdir}/cmake/Qt5Designer/



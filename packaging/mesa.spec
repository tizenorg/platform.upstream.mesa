%define glamor 1
%bcond_with x
%bcond_with wayland

Name:           mesa
Version:        10.3
Release:        0
License:        MIT
Summary:        System for rendering interactive 3-D graphics
Url:            http://www.mesa3d.org
Group:          Graphics & UI Framework/Hardware Adaptation
Source:         MesaLib-%{version}.tar.bz2
Source2:        baselibs.conf
Source3:        README.updates
Source5:        drirc
Source6:        %{name}-rpmlintrc
Source1001:     mesa.manifest
BuildRequires:  autoconf >= 2.59
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  gettext-tools
BuildRequires:  libtool
BuildRequires:  libxml2-python
BuildRequires:  llvm-devel
%if %{with x}
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(dri2proto)
BuildRequires:  pkgconfig(glproto)
BuildRequires:  pkgconfig(xcb-dri2)
BuildRequires:  pkgconfig(xcb-glx)
%endif
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  python-lxml
BuildRequires:  python-xml
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(libdrm) >= 2.4.24
%ifarch x86_64 %ix86
BuildRequires:  pkgconfig(libdrm_intel) >= 2.4.24
%endif
BuildRequires:  pkgconfig(libudev) > 150
%if %{with wayland}
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-server)
%endif
Provides:       Mesa = %{version}

%description
Mesa is a 3-D graphics library with an API which is very similar to
that of OpenGL.* To the extent that Mesa utilizes the OpenGL command
syntax or state machine, it is being used with authorization from
Silicon Graphics, Inc.(SGI). However, the author does not possess an
OpenGL license from SGI, and makes no claim that Mesa is in any way a
compatible replacement for OpenGL or associated with SGI. Those who
want a licensed implementation of OpenGL should contact a licensed
vendor.

Please do not refer to the library as MesaGL (for legal reasons). It's
just Mesa or The Mesa 3-D graphics library.

* OpenGL is a trademark of Silicon Graphics Incorporated.

%package devel
Summary:        Libraries, includes and more to develop Mesa applications
Requires:       mesa = %{version}
Requires:       mesa-libEGL-devel = %{version}
Requires:       mesa-libGLESv1_CM-devel = %{version}
Requires:       mesa-libGLESv2-devel = %{version}
Requires:       mesa-libglapi = %{version}
Requires:       libgbm-devel
%if %{with wayland}
Requires:       libwayland-egl
%endif
%if %{with x}
Requires:       mesa-libGL-devel = %{version}
%endif

%description devel
Mesa is a 3-D graphics library with an API which is very similar to
that of OpenGL.* To the extent that Mesa utilizes the OpenGL command
syntax or state machine, it is being used with authorization from
Silicon Graphics, Inc.(SGI). However, the author does not possess an
OpenGL license from SGI, and makes no claim that Mesa is in any way a
compatible replacement for OpenGL or associated with SGI. Those who
want a licensed implementation of OpenGL should contact a licensed
vendor.

Please do not refer to the library as MesaGL (for legal reasons). It's
just Mesa or The Mesa 3-D graphics library.

* OpenGL is a trademark of Silicon Graphics Incorporated.

%if %{with x}
%package -n mesa-libGL
Summary:        Free implementation of the desktop GL API

%description -n mesa-libGL
This package contains the GL native platform graphics interface
library. GL provides a desktop-oriented API for creating
rendering surfaces. It depends on X11.

%package -n mesa-libGL-devel
Summary:        Development files for the desktop GL API
Requires:       mesa-libGL = %{version}

%description -n mesa-libGL-devel
This package contains the GL native platform graphics interface
library. GL provides a desktop-oriented API for creating
rendering surfaces. It depends on X11.

This package provides the development environment for compiling
programs against the GL library.
%endif

%package -n libwayland-egl
Summary:        Wayland EGL backend for Mesa

%description -n libwayland-egl
Wayland EGL backend for Mesa.

%package -n mesa-libEGL
# Kudos to Debian for the descriptions
Summary:        Free implementation of the EGL API

%description -n mesa-libEGL
This package contains the EGL native platform graphics interface
library. EGL provides a platform-agnostic mechanism for creating
rendering surfaces for use with other graphics libraries, such as
OpenGL|ES and OpenVG.

This package contains modules to interface with the existing system
GLX or DRI2 drivers to provide OpenGL via EGL. The Mesa main package
provides drivers to provide hardware-accelerated OpenGL|ES and OpenVG
support.

%package -n mesa-libEGL-devel
Summary:        Development files for the EGL API
Requires:       mesa-libEGL = %{version}
# Other requires taken care of by pkgconfig already

%description -n mesa-libEGL-devel
This package contains the development environment required for
compiling programs against EGL native platform graphics interface
library. EGL provides a platform-agnostic mechanism for creating
rendering surfaces for use with other graphics libraries, such as
OpenGL|ES and OpenVG.

This package provides the development environment for compiling
programs against the EGL library.

%ifarch %ix86 x86_64
%package -n mesa-gallium-pipe
# Kudos to Debian for the descriptions
Summary:        Free implementation of Gallium-pipe API

%description -n mesa-gallium-pipe
Gallium

%package -n libxatracker
Summary:   XA state tracker
Group:     System/Libraries
Provides:  xatracker

%description -n libxatracker
This package contains the XA state tracker for gallium3D driver.
It superseeds the Xorg state tracker and provides an infrastructure
to accelerate Xorg 2D operations. It is currently used by vmwgfx
video driver.

%package -n libxatracker-devel
Summary:        Development files for the XA API
Group:          Development/Libraries/C and C++
Requires:       libxatracker = %version

%description -n libxatracker-devel
This package contains the XA state tracker for gallium3D driver.
It superseeds the Xorg state tracker and provides an infrastructure
to accelerate Xorg 2D operations. It is currently used by vmwgfx
video driver.

This package provides the development environment for compiling
programs against the XA state tracker.
%endif

%package -n mesa-libGLESv1_CM
Summary:        Free implementation of the OpenGL|ES 1.x API

%description -n mesa-libGLESv1_CM
OpenGL|ES is a cross-platform API for full-function 2D and 3D
graphics on embedded systems - including consoles, phones, appliances
and vehicles. It contains a subset of OpenGL plus a number of
extensions for the special needs of embedded systems.

OpenGL|ES 1.x provides an API for fixed-function hardware.

%package -n mesa-libGLESv1_CM-devel
Summary:        Development files for the EGL API
Requires:       mesa-libGLESv1_CM = %{version}
Requires:       pkgconfig(egl)

%description -n mesa-libGLESv1_CM-devel
OpenGL|ES is a cross-platform API for full-function 2D and 3D
graphics on embedded systems - including consoles, phones, appliances
and vehicles. It contains a subset of OpenGL plus a number of
extensions for the special needs of embedded systems.

OpenGL|ES 1.x provides an API for fixed-function hardware.

This package provides a development environment for building programs
using the OpenGL|ES 1.x APIs.

%package -n mesa-libGLESv2
Summary:        Free implementation of the OpenGL|ES 2.x API

%description -n mesa-libGLESv2
OpenGL|ES is a cross-platform API for full-function 2D and 3D
graphics on embedded systems - including consoles, phones, appliances
and vehicles. It contains a subset of OpenGL plus a number of
extensions for the special needs of embedded systems.

OpenGL|ES 2.x provides an API for programmable hardware including
vertex and fragment shaders.

%package -n mesa-libGLESv2-devel
Summary:        Development files for the EGL API
Requires:       mesa-libGLESv2 = %{version}
Requires:       pkgconfig(egl)

%description -n mesa-libGLESv2-devel
OpenGL|ES is a cross-platform API for full-function 2D and 3D
graphics on embedded systems - including consoles, phones, appliances
and vehicles. It contains a subset of OpenGL plus a number of
extensions for the special needs of embedded systems.

OpenGL|ES 2.x provides an API for programmable hardware including
vertex and fragment shaders.

This package provides a development environment for building
applications using the OpenGL|ES 2.x APIs.

%package -n mesa-libGLESv3-devel
Summary:        Development files for the OpenGL ES 3.x API
Requires:       pkgconfig(egl)

%description -n mesa-libGLESv3-devel
OpenGL|ES is a cross-platform API for full-function 2D and 3D
graphics on embedded systems - including consoles, phones, appliances
and vehicles. It contains a subset of OpenGL plus a number of
extensions for the special needs of embedded systems.

This package provides a development environment for building
applications using the OpenGL|ES 3.x APIs.

%package -n libgbm
Summary:        Generic buffer management API

%description -n libgbm
This package contains the GBM buffer management library. It provides
a mechanism for allocating buffers for graphics rendering tied to
Mesa.

GBM is intended to be used as a native platform for EGL on drm or
openwfd.

%package -n libgbm-devel
Summary:        Development files for the EGL API
Requires:       libgbm = %{version}

%description -n libgbm-devel
This package contains the GBM buffer management library. It provides
a mechanism for allocating buffers for graphics rendering tied to
Mesa.

GBM is intended to be used as a native platform for EGL on drm or
openwfd.

This package provides the development environment for compiling
programs against the GBM library.

%package -n mesa-libglapi
Summary:        Free implementation of the GL API

%description -n mesa-libglapi
The Mesa GL API module is responsible for dispatching all the gl*
functions. It is intended to be mainly used by the Mesa-libGLES*
packages.

%prep
%setup -q
cp %{SOURCE1001} .

rm -rf docs/README.{VMS,WIN32,OS2}

%build

%install
rm -f src/mesa/depend
autoreconf -fi
%configure --enable-gles1 \
           --enable-gles2 \
           --disable-dri3 \
%if %{with x}
%if %{with wayland}
           --with-egl-platforms=drm,wayland,x11 \
%else
           --with-egl-platforms=drm,x11 \
%endif
%else
%if %{with wayland}
           --with-egl-platforms=drm,wayland \
           --disable-glx \
%else
           --with-egl-platforms=drm \
           --disable-glx \
%endif
%endif
           --enable-shared-glapi \
           --enable-texture-float \
%if %glamor
           --enable-gbm \
%endif
           --with-dri-searchpath=/usr/%{_lib}/dri/updates:/usr/%{_lib}/dri \
%ifarch %ix86 x86_64
           --enable-gallium-egl \
           --enable-gallium-llvm \
           --with-dri-drivers=i915,i965,swrast \
           --with-gallium-drivers="i915,svga,swrast" \
           --enable-xa \
%else
           --disable-gallium-egl \
%endif
%ifarch %arm aarch64
           --with-dri-drivers=swrast \
           --with-gallium-drivers="" \
%endif
           CFLAGS="%{optflags} -DNDEBUG"
make %{?_smp_mflags}
%make_install

%if !%{with x}
rm -rf %{buildroot}%{_includedir}/GL
rm -f %{buildroot}%{_libdir}/pkgconfig/gl.pc
%endif

# DRI driver update mechanism
mkdir -p %{buildroot}%{_libdir}/dri/updates
install -m 644 $RPM_SOURCE_DIR/README.updates \
  %{buildroot}%{_libdir}/dri/updates
# global drirc file
mkdir -p %{buildroot}/etc
install -m 644 $RPM_SOURCE_DIR/drirc %{buildroot}/etc


%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post   -n libwayland-egl -p /sbin/ldconfig

%postun -n libwayland-egl -p /sbin/ldconfig

%post   -n mesa-libEGL -p /sbin/ldconfig

%postun -n mesa-libEGL -p /sbin/ldconfig

%ifarch %ix86 x86_64
%post   -n mesa-gallium-pipe -p /sbin/ldconfig
%postun -n mesa-gallium-pipe -p /sbin/ldconfig
%endif

%post   -n mesa-libGLESv1_CM -p /sbin/ldconfig

%postun -n mesa-libGLESv1_CM -p /sbin/ldconfig

%post   -n mesa-libGLESv2 -p /sbin/ldconfig

%postun -n mesa-libGLESv2 -p /sbin/ldconfig

%post   -n libgbm -p /sbin/ldconfig

%postun -n libgbm -p /sbin/ldconfig

%post   -n mesa-libglapi -p /sbin/ldconfig

%postun -n mesa-libglapi -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license docs/COPYING
%config %{_sysconfdir}/drirc
%{_libdir}/dri/

%if %{with x}
%files -n mesa-libGL
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libGL.so.1*

%files -n mesa-libGL-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/GL
%{_libdir}/libGL.so
%{_libdir}/pkgconfig/gl.pc
%endif

%files -n mesa-libEGL
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libEGL.so.1*
%ifarch %ix86 x86_64
%{_libdir}/egl/egl_gallium.so
%endif

%files -n mesa-libEGL-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/EGL
%{_includedir}/KHR
%{_libdir}/libEGL.so
%{_libdir}/pkgconfig/egl.pc

%ifarch %ix86 x86_64
%files -n mesa-gallium-pipe
%manifest %{name}.manifest
%defattr(-,root,root)

%files -n libxatracker
%defattr(-,root,root)
%manifest %{name}.manifest
%_libdir/libxatracker.so.*

%files -n libxatracker-devel
%defattr(-,root,root)
%manifest %{name}.manifest
%_includedir/xa_*.h
%_libdir/libxatracker.so
%_libdir/pkgconfig/xatracker.pc
%endif

%files -n mesa-libGLESv1_CM
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libGLESv1_CM.so.1*

%files -n mesa-libGLESv1_CM-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/GLES
%{_libdir}/libGLESv1_CM.so
%{_libdir}/pkgconfig/glesv1_cm.pc

%files -n mesa-libGLESv2
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libGLESv2.so.2*

%files -n mesa-libGLESv2-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/GLES2
%{_libdir}/libGLESv2.so
%{_libdir}/pkgconfig/glesv2.pc

%files -n mesa-libGLESv3-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/GLES3

%if %{with wayland}

%files -n libwayland-egl
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libwayland-egl.so.1*

%endif

%files -n libgbm
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libgbm.so.1*
%ifarch %ix86 x86_64
%{_libdir}/gbm/gbm_gallium_drm.so
%endif

%files -n libgbm-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/gbm.h
%{_libdir}/libgbm.so
%{_libdir}/pkgconfig/gbm.pc


%files -n mesa-libglapi
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libglapi.so.0*

%files devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libglapi.so
%if %{with wayland}
%{_libdir}/libwayland-egl.so
%{_libdir}/pkgconfig/wayland-egl.pc
%endif
%{_libdir}/pkgconfig/dri.pc

%changelog

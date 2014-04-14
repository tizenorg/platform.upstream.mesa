%define glamor 1
%bcond_with wayland
%bcond_with x

Name:           mesa
Version:        9.2.1
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
BuildRequires:  pkgconfig
BuildRequires:  python
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
%if %{with x}
BuildRequires:  makedepend
BuildRequires:  pkgconfig(dri2proto) >= 2.1
BuildRequires:  pkgconfig(glproto) >= 1.4.11
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-dri2)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xvmc)
BuildRequires:  pkgconfig(xxf86vm)
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
Requires:       mesa-libIndirectGL = %{version}
Requires:       libOSMesa = %{version}
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

%package -n mesa-gallium-pipe
# Kudos to Debian for the descriptions
Summary:        Free implementation of Gallium-pipe API

%description -n mesa-gallium-pipe
Gallium

%if %{with x}
%package -n mesa-libGL
Summary:        The GL/GLX runtime of the Mesa 3D graphics library
Requires:       mesa = %{version}

%description -n mesa-libGL
Mesa is a software library for 3D computer graphics that provides a
generic OpenGL implementation for rendering three-dimensional
graphics.

GLX ("OpenGL Extension to the X Window System") provides the
interface connecting OpenGL and the X Window System: it enables
programs wishing to use OpenGL to do so within a window provided by
the X Window System.

%package -n mesa-libGL-devel
Summary:        GL/GLX development files of the OpenGL API
Requires:       mesa-libGL = %{version}

%description -n mesa-libGL-devel
Mesa is a software library for 3D computer graphics that provides a
generic OpenGL implementation for rendering three-dimensional
graphics.

This package includes headers and static libraries for compiling
programs with Mesa.
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

%if %{with x}
%package -n mesa-libIndirectGL
# This is the equivalent to Debian's libgl1-mesa-swx11
Summary:        Free implementation of the OpenGL API

%description -n mesa-libIndirectGL
This library provides a pure software rasterizer; it does not provide
a direct rendering capable library, or one which uses GLX. For that,
please see Mesa-libGL1.

%package -n mesa-libIndirectGL-devel
Summary:        Development Files for the free implementation of the OpenGL API
Requires:       mesa-libIndirectGL = %{version}

%description -n mesa-libIndirectGL-devel
This library provides a pure software rasterizer; it does not provide
a direct rendering capable library, or one which uses GLX. For that,
please see Mesa-libGL1.

%package -n libOSMesa
Summary:        Mesa Off-screen rendering extension

%description -n libOSMesa
OSmesa is a Mesa extension that allows programs to render to an
off-screen buffer using the OpenGL API without having to create a
rendering context on an X Server. It uses a pure software renderer.
%endif

%package -n libgbm
# as per gbm.pc
Version:        0.0.0
Release:        0
Summary:        Generic buffer management API

%description -n libgbm
This package contains the GBM buffer management library. It provides
a mechanism for allocating buffers for graphics rendering tied to
Mesa.

GBM is intended to be used as a native platform for EGL on drm or
openwfd.

%package -n libgbm-devel
Version:        0.0.0
Release:        0
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

%if %{with x}
%package -n libxatracker
Version:        1.0.0
Release:        0
Summary:        XA state tracker

%description -n libxatracker
This package contains the XA state tracker for gallium3D driver.
It superseeds the Xorg state tracker and provides an infrastructure
to accelerate Xorg 2D operations. It is currently used by vmwgfx
video driver.

%package -n libxatracker-devel
Version:        1.0.0
Release:        0
Summary:        Development files for the XA API
Requires:       libxatracker = %{version}

%description -n libxatracker-devel
This package contains the XA state tracker for gallium3D driver.
It superseeds the Xorg state tracker and provides an infrastructure
to accelerate Xorg 2D operations. It is currently used by vmwgfx
video driver.

This package provides the development environment for compiling
programs against the XA state tracker.

%package -n libXvMC_softpipe
Summary:        Software implementation of XVMC state tracker

%description -n libXvMC_softpipe
This package contains the Software implementation of the XvMC
state tracker. This is still "work in progress", i.e. expect
poor video quality, choppy videos and artefacts all over.

%package -n libvdpau_softpipe
Summary:        Software implementation of XVMC state tracker

%description -n libvdpau_softpipe
This package contains the Software implementation of the VDPAU
state tracker. This is still "work in progress", i.e. expect
poor video quality, choppy videos and artefacts all over.
%endif

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
%if %{with wayland}
%if !%{with x}
           --with-egl-platforms=wayland,drm \
           --disable-glx \
%else
           --with-egl-platforms=wayland,drm,x11 \
%endif
%else
           --with-egl-platforms=x11,drm \
%endif
           --enable-shared-glapi \
%if %{with x}
           --enable-xa \
%endif
           --enable-texture-float \
%if %glamor
           --enable-gbm \
%if %{with x}
           --enable-glx-tls \
%endif
%endif
           --with-dri-searchpath=/usr/%{_lib}/dri/updates:/usr/%{_lib}/dri \
%ifarch %ix86 x86_64
           --enable-gallium-egl \
           --enable-gallium-llvm \
           --with-dri-drivers=i915,i965,swrast \
           --with-gallium-drivers="i915,svga,swrast" \
%if %{with x}
           --enable-xvmc \
%endif
%endif
%ifarch %arm
           --with-dri-drivers=swrast \
           --with-gallium-drivers="" \
%endif
           CFLAGS="%{optflags} -DNDEBUG"
make %{?_smp_mflags}
%make_install

%if %{with wayland} && !%{with x}
rm -rf %{buildroot}%{_includedir}/GL
rm -f %{buildroot}%{_libdir}/pkgconfig/gl.pc
%endif

%if %{with x}
# build and install Indirect Rendering only libGL

make clean
%configure --enable-xlib-glx \
           --enable-osmesa \
           --disable-dri \
           --with-egl-platforms=x11 \
           --with-gallium-drivers="" \
           --with-gl-lib-name=IndirectGL \
           CFLAGS="%{optflags} -DNDEBUG"

make %{?_smp_mflags}
cp -a \
   src/mesa/drivers/x11/.libs/libIndirectGL.so* \
   src/mesa/drivers/osmesa/.libs/libOSMesa.so* \
   %{buildroot}%{_libdir}
install -m 644 src/mesa/drivers/osmesa/osmesa.pc \
   %{buildroot}%{_libdir}/pkgconfig

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

%post   -n mesa-gallium-pipe -p /sbin/ldconfig

%postun -n mesa-gallium-pipe -p /sbin/ldconfig

%post   -n mesa-libGLESv1_CM -p /sbin/ldconfig

%postun -n mesa-libGLESv1_CM -p /sbin/ldconfig

%post   -n mesa-libGLESv2 -p /sbin/ldconfig

%postun -n mesa-libGLESv2 -p /sbin/ldconfig

%if %{with x}
%post   -n mesa-libGL -p /sbin/ldconfig

%postun -n mesa-libGL -p /sbin/ldconfig

%post   -n mesa-libIndirectGL -p /sbin/ldconfig

%postun -n mesa-libIndirectGL -p /sbin/ldconfig

%post   -n libOSMesa -p /sbin/ldconfig

%postun -n libOSMesa -p /sbin/ldconfig

%ifnarch  %arm
%post   -n libxatracker -p /sbin/ldconfig

%postun -n libxatracker -p /sbin/ldconfig



%post   -n libXvMC_softpipe -p /sbin/ldconfig

%postun -n libXvMC_softpipe -p /sbin/ldconfig

%endif

%endif

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
%{_libdir}/libdricore9*.so.*

%files -n mesa-libEGL
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libEGL.so.1*
%{_libdir}/egl/egl_gallium.so

%files -n mesa-libEGL-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/EGL
%{_includedir}/KHR
%{_libdir}/libEGL.so
%{_libdir}/pkgconfig/egl.pc

%files -n mesa-gallium-pipe
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/gallium-pipe/*

%if %{with x}
%files -n mesa-libGL
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libGL.so.1*

%files -n mesa-libGL-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%dir %{_includedir}/GL
%{_includedir}/GL/*.h
%{_libdir}/libGL.so
%{_libdir}/pkgconfig/gl.pc
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

%if %{with wayland}

%files -n libwayland-egl
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libwayland-egl.so.1*

%endif

%if %{with x}
%files -n mesa-libIndirectGL
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libIndirectGL.so.1*

%files -n mesa-libIndirectGL-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libIndirectGL.so

%files -n libOSMesa
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libOSMesa.so.8*

%ifnarch %arm

%files -n libxatracker
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libxatracker.so.1*

%files -n libxatracker-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/xa_*.h
%{_libdir}/libxatracker.so
%{_libdir}/pkgconfig/xatracker.pc


%files -n libXvMC_softpipe
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libXvMCsoftpipe.so
%{_libdir}/libXvMCsoftpipe.so.1
%{_libdir}/libXvMCsoftpipe.so.1.0.0

%endif

%endif

%files -n libgbm
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libgbm.so.1*
%{_libdir}/gbm/gbm_gallium_drm.so

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
%if %{with x}
%{_includedir}/GL/internal
%endif
%{_libdir}/libglapi.so
%if %{with wayland}
%{_libdir}/libwayland-egl.so
%{_libdir}/pkgconfig/wayland-egl.pc
%endif
%if %{with x}
%{_libdir}/libOSMesa.so
%{_libdir}/pkgconfig/osmesa.pc
%endif
%{_libdir}/pkgconfig/dri.pc
%{_libdir}/libdricore9*.so

%files -n mesa-libGLESv3-devel
%manifest %{name}.manifest
%defattr(-,root,root)
%{_includedir}/GLES3

%changelog

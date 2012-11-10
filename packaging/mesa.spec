%define glamor 1
%define enable_wayland 0

#
%define _version 9.0
%define _name_archive MesaLib

Name:           mesa
Version:        9.0
Release:        0
BuildRequires: makedepend
BuildRequires:  autoconf >= 2.59
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  expat-devel
#BuildRequires:  libtalloc-devel
BuildRequires:  libtool
BuildRequires:  libxml2-python
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  pkgconfig(dri2proto) >= 2.1
BuildRequires:  pkgconfig(glproto) >= 1.4.11
BuildRequires:  pkgconfig(libdrm) >= 2.4.24
%ifarch x86_64 %ix86
BuildRequires:  pkgconfig(libdrm_intel) >= 2.4.24
%endif
BuildRequires:  pkgconfig(libudev) > 150
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xcb-dri2)
BuildRequires:  pkgconfig(xcb-glx)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xxf86vm)
%if 0%{?enable_wayland}
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-server)
%endif
BuildRequires:  libXvMC-devel
Url:            http://www.mesa3d.org
Summary:        System for rendering interactive 3-D graphics
License:        MIT
Group:          System/Libraries
Source:         %{_name_archive}-%{_version}.tar.bz2
Source2:        baselibs.conf
Source3:        README.updates
Source5:        drirc
Source6:        %name-rpmlintrc
# do not put dates in sources to fix build-compare
Patch1:         Mesa-nodate.diff
Provides:	Mesa = %version

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
Group:          Development/Libraries/X11
Requires:       mesa = %version
Requires:       mesa-libEGL-devel = %version
Requires:       mesa-libGL-devel = %version
Requires:       mesa-libGLESv1_CM-devel = %version
Requires:       mesa-libGLESv2-devel = %version
Requires:       mesa-libIndirectGL = %version
Requires:       mesa-libglapi = %version
%if 0%{?enable_wayland}
Requires:	libwayland-egl 
%endif
Requires:       libOSMesa = %version
Requires:       libgbm-devel

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
Summary:	Wayland EGL backend for Mesa
Group:		System/Libraries

%description -n libwayland-egl
Wayland EGL backend for Mesa.

%package -n mesa-libEGL
# Kudos to Debian for the descriptions
Summary:        Free implementation of the EGL API
Group:          System/Libraries

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
Group:          Development/Libraries/C and C++
Requires:       mesa-libEGL = %version
# Other requires taken care of by pkgconfig already

%description -n mesa-libEGL-devel
This package contains the development environment required for
compiling programs against EGL native platform graphics interface
library. EGL provides a platform-agnostic mechanism for creating
rendering surfaces for use with other graphics libraries, such as
OpenGL|ES and OpenVG.

This package provides the development environment for compiling
programs against the EGL library.

%package -n mesa-libGL
Summary:        The GL/GLX runtime of the Mesa 3D graphics library
Group:          System/Libraries
Requires:       mesa = %version

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
Group:          Development/Libraries/C and C++
Requires:       mesa-libGL = %version

%description -n mesa-libGL-devel
Mesa is a software library for 3D computer graphics that provides a
generic OpenGL implementation for rendering three-dimensional
graphics.

This package includes headers and static libraries for compiling
programs with Mesa.

%package -n mesa-libGLESv1_CM
Summary:        Free implementation of the OpenGL|ES 1.x API
Group:          System/Libraries

%description -n mesa-libGLESv1_CM
OpenGL|ES is a cross-platform API for full-function 2D and 3D
graphics on embedded systems - including consoles, phones, appliances
and vehicles. It contains a subset of OpenGL plus a number of
extensions for the special needs of embedded systems.

OpenGL|ES 1.x provides an API for fixed-function hardware.

%package -n mesa-libGLESv1_CM-devel
Summary:        Development files for the EGL API
Group:          Development/Libraries/C and C++
Requires:       mesa-libGLESv1_CM = %version
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
Group:          System/Libraries

%description -n mesa-libGLESv2
OpenGL|ES is a cross-platform API for full-function 2D and 3D
graphics on embedded systems - including consoles, phones, appliances
and vehicles. It contains a subset of OpenGL plus a number of
extensions for the special needs of embedded systems.

OpenGL|ES 2.x provides an API for programmable hardware including
vertex and fragment shaders.

%package -n mesa-libGLESv2-devel
Summary:        Development files for the EGL API
Group:          Development/Libraries/C and C++
Requires:       mesa-libGLESv2 = %version
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


%package -n mesa-libIndirectGL
# This is the equivalent to Debian's libgl1-mesa-swx11
Summary:        Free implementation of the OpenGL API
Group:          System/Libraries

%description -n mesa-libIndirectGL
This library provides a pure software rasterizer; it does not provide
a direct rendering capable library, or one which uses GLX. For that,
please see Mesa-libGL1.


%package -n mesa-libIndirectGL-devel
Summary:        Development Files for the free implementation of the OpenGL API
Group:          Development/Libraries/C and C++
Requires:       mesa-libIndirectGL1 = %version

%description -n mesa-libIndirectGL-devel
This library provides a pure software rasterizer; it does not provide
a direct rendering capable library, or one which uses GLX. For that,
please see Mesa-libGL1.


%package -n libOSMesa
Summary:        Mesa Off-screen rendering extension
Group:          System/Libraries

%description -n libOSMesa
OSmesa is a Mesa extension that allows programs to render to an
off-screen buffer using the OpenGL API without having to create a
rendering context on an X Server. It uses a pure software renderer.

%package -n libgbm
Summary:        Generic buffer management API
Group:          System/Libraries
# as per gbm.pc
Version:        0.0.0
Release:        0

%description -n libgbm
This package contains the GBM buffer management library. It provides
a mechanism for allocating buffers for graphics rendering tied to
Mesa.

GBM is intended to be used as a native platform for EGL on drm or
openwfd.

%package -n libgbm-devel
Summary:        Development files for the EGL API
Group:          Development/Libraries/C and C++
Version:        0.0.0
Release:        0
Requires:       libgbm = %version

%description -n libgbm-devel
This package contains the GBM buffer management library. It provides
a mechanism for allocating buffers for graphics rendering tied to
Mesa.

GBM is intended to be used as a native platform for EGL on drm or
openwfd.

This package provides the development environment for compiling
programs against the GBM library.

%package -n libxatracker
Summary:        XA state tracker
Group:          System/Libraries
Version:        1.0.0
Release:        0

%description -n libxatracker
This package contains the XA state tracker for gallium3D driver.
It superseeds the Xorg state tracker and provides an infrastructure
to accelerate Xorg 2D operations. It is currently used by vmwgfx 
video driver.

%package -n libxatracker-devel
Summary:        Development files for the XA API
Group:          Development/Libraries/C and C++
Version:        1.0.0
Release:        0
Requires:       libxatracker = %version

%description -n libxatracker-devel
This package contains the XA state tracker for gallium3D driver.
It superseeds the Xorg state tracker and provides an infrastructure
to accelerate Xorg 2D operations. It is currently used by vmwgfx 
video driver.

This package provides the development environment for compiling
programs against the XA state tracker.


%package -n libXvMC_softpipe
Summary:        Software implementation of XVMC state tracker
Group:          System/Libraries

%description -n libXvMC_softpipe
This package contains the Software implementation of the XvMC
state tracker. This is still "work in progress", i.e. expect
poor video quality, choppy videos and artefacts all over.


%package -n libvdpau_softpipe
Summary:        Software implementation of XVMC state tracker
Group:          System/Libraries

%description -n libvdpau_softpipe
This package contains the Software implementation of the VDPAU
state tracker. This is still "work in progress", i.e. expect
poor video quality, choppy videos and artefacts all over.

%package -n mesa-libglapi
Summary:        Free implementation of the GL API
Group:          System/Libraries

%description -n mesa-libglapi
The Mesa GL API module is responsible for dispatching all the gl*
functions. It is intended to be mainly used by the Mesa-libGLES*
packages.


%prep
%setup -n MesaLib-%{_version}  -q

rm -rf docs/README.{VMS,WIN32,OS2}

%build

%install
rm -f src/mesa/depend
autoreconf -fi
%configure --enable-gles1 \
           --enable-gles2 \
%if 0%{?enable_wayland}
           --with-egl-platforms=x11,drm,wayland \
%else
           --with-egl-platforms=x11,drm \
%endif
           --enable-shared-glapi \
           --enable-xa \
           --enable-texture-float \
	   --enable-glu \
%if %glamor
           --enable-gbm \
           --enable-glx-tls \
%endif
           --with-dri-searchpath=/usr/%{_lib}/dri/updates:/usr/%{_lib}/dri \
%ifarch %ix86 x86_64
           --enable-gallium-llvm \
           --with-dri-drivers=i915,i965 \
           --with-gallium-drivers=swrast,svga \
           --enable-xvmc \
%endif
%ifarch %arm
           --with-dri-drivers=swrast \
           --with-gallium-drivers="" \
%endif
           CFLAGS="$RPM_OPT_FLAGS -DNDEBUG"
make %{?_smp_mflags}
%make_install
# build and install Indirect Rendering only libGL

make clean-local
%configure --enable-xlib-glx \
           --enable-osmesa \
           --disable-dri \
           --with-egl-platforms=x11 \
           --with-gallium-drivers="" \
           --with-gl-lib-name=IndirectGL \
           CFLAGS="$RPM_OPT_FLAGS -DNDEBUG"

make %{?_smp_mflags}
cp -a \
   src/mesa/drivers/x11/.libs/libIndirectGL.so* \
   src/mesa/drivers/osmesa/.libs/libOSMesa.so* \
   $RPM_BUILD_ROOT/usr/%{_lib}
install -m 644 src/mesa/drivers/osmesa/osmesa.pc \
   $RPM_BUILD_ROOT/usr/%{_lib}/pkgconfig

# DRI driver update mechanism
mkdir -p $RPM_BUILD_ROOT/usr/%{_lib}/dri/updates
install -m 644 $RPM_SOURCE_DIR/README.updates \
  $RPM_BUILD_ROOT/usr/%{_lib}/dri/updates
# global drirc file
mkdir -p $RPM_BUILD_ROOT/etc
install -m 644 $RPM_SOURCE_DIR/drirc $RPM_BUILD_ROOT/etc


%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post   -n libwayland-egl -p /sbin/ldconfig

%postun -n libwayland-egl -p /sbin/ldconfig

%post   -n mesa-libEGL -p /sbin/ldconfig

%postun -n mesa-libEGL -p /sbin/ldconfig

%post   -n mesa-libGL -p /sbin/ldconfig

%postun -n mesa-libGL -p /sbin/ldconfig

%post   -n mesa-libGLESv1_CM -p /sbin/ldconfig

%postun -n mesa-libGLESv1_CM -p /sbin/ldconfig

%post   -n mesa-libGLESv2 -p /sbin/ldconfig

%postun -n mesa-libGLESv2 -p /sbin/ldconfig

%post   -n mesa-libIndirectGL -p /sbin/ldconfig

%postun -n mesa-libIndirectGL -p /sbin/ldconfig

%post   -n libOSMesa -p /sbin/ldconfig

%postun -n libOSMesa -p /sbin/ldconfig

%post   -n libgbm -p /sbin/ldconfig

%postun -n libgbm -p /sbin/ldconfig

%ifnarch  %arm

%post   -n libxatracker -p /sbin/ldconfig

%postun -n libxatracker -p /sbin/ldconfig



%post   -n libXvMC_softpipe
%postun -n libXvMC_softpipe

%endif

%post   -n mesa-libglapi -p /sbin/ldconfig

%postun -n mesa-libglapi -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc docs/README* docs/COPYING
%config /etc/drirc
%{_libdir}/dri/
%_libdir/libdricore9*.so.*

%files -n mesa-libEGL
%defattr(-,root,root)
%_libdir/libEGL.so.1*

%files -n mesa-libEGL-devel
%defattr(-,root,root)
%_includedir/EGL
%_includedir/KHR
%_libdir/libEGL.so
%_libdir/pkgconfig/egl.pc

%files -n mesa-libGL
%defattr(-,root,root)
%_libdir/libGL.so.1*

%files -n mesa-libGL-devel
%defattr(-,root,root)
%dir %_includedir/GL
%_includedir/GL/*.h
%_libdir/libGL.so
%_libdir/pkgconfig/gl.pc

%files -n mesa-libGLESv1_CM
%defattr(-,root,root)
%_libdir/libGLESv1_CM.so.1*

%files -n mesa-libGLESv1_CM-devel
%defattr(-,root,root)
%_includedir/GLES
%_libdir/libGLESv1_CM.so
%_libdir/pkgconfig/glesv1_cm.pc

%files -n mesa-libGLESv2
%defattr(-,root,root)
%_libdir/libGLESv2.so.2*

%files -n mesa-libGLESv2-devel
%defattr(-,root,root)
%_includedir/GLES2
%_libdir/libGLESv2.so
%_libdir/pkgconfig/glesv2.pc


%files -n mesa-libIndirectGL
%defattr(-,root,root)
%_libdir/libIndirectGL.so.1*

%files -n mesa-libIndirectGL-devel
%defattr(-,root,root)
%_libdir/libIndirectGL.so

%files -n libOSMesa
%defattr(-,root,root)
%_libdir/libOSMesa.so.8*

%if 0%{?enable_wayland}
%files -n libwayland-egl
%defattr(-,root,root)
%_libdir/libwayland-egl.so.1*
%endif

%files -n libgbm
%defattr(-,root,root)
%_libdir/libgbm.so.1*

%files -n libgbm-devel
%defattr(-,root,root)
%_includedir/gbm.h
%_libdir/libgbm.so
%_libdir/pkgconfig/gbm.pc

%ifnarch %arm

%files -n libxatracker
%defattr(-,root,root)
%_libdir/libxatracker.so.1*

%files -n libxatracker-devel
%defattr(-,root,root)
%_includedir/xa_*.h
%_libdir/libxatracker.so
%_libdir/pkgconfig/xatracker.pc


%files -n libXvMC_softpipe
%defattr(-,root,root)
%_libdir/libXvMCsoftpipe.so
%_libdir/libXvMCsoftpipe.so.1
%_libdir/libXvMCsoftpipe.so.1.0

%endif

%files -n mesa-libglapi
%defattr(-,root,root)
%_libdir/libglapi.so.0*

%files devel
%defattr(-,root,root)
%_includedir/GL/internal
%_libdir/libOSMesa.so
%_libdir/libglapi.so
%_libdir/pkgconfig/osmesa.pc
%if 0%{?enable_wayland}
%_libdir/libwayland-egl.so
%_libdir/pkgconfig/wayland-egl.pc
%endif
%_libdir/pkgconfig/dri.pc
%_libdir/libdricore9*.so

%changelog

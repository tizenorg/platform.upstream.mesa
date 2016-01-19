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

%if "%{_with_emulator}" == "1"
ExclusiveArch:
%else
ExclusiveArch: %{ix86} x86_64
%endif

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
Summary:        Wayland EGL backend

%description -n libwayland-egl
Wayland EGL backend for Mesa.

%package -n libwayland-egl-devel
Summary:        Development files for use with Wayland protocol

%description -n libwayland-egl-devel
Development files for use with Wayland protocol

%prep
%setup -q
cp %{SOURCE1001} .

rm -rf docs/README.{VMS,WIN32,OS2}

%build

rm -f src/mesa/depend
%reconfigure --enable-gles1 \
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

%__make %{?_smp_mflags}

%install
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

# remove include files
rm -rf %{buildroot}%{_includedir}/EGL
rm -rf %{buildroot}%{_includedir}/GLES
rm -rf %{buildroot}%{_includedir}/GLES2
rm -rf %{buildroot}%{_includedir}/GLES3
rm -rf %{buildroot}%{_includedir}/KHR
rm -f %{buildroot}%{_includedir}/gbm.h
rm -f %{buildroot}%{_includedir}/xa_composite.h
rm -f %{buildroot}%{_includedir}/xa_context.h
rm -f %{buildroot}%{_includedir}/xa_tracker.h

# remove package config files
rm -f %{buildroot}%{_libdir}/pkgconfig/dri.pc
rm -f %{buildroot}%{_libdir}/pkgconfig/egl.pc
rm -f %{buildroot}%{_libdir}/pkgconfig/gbm.pc
rm -f %{buildroot}%{_libdir}/pkgconfig/glesv1_cm.pc
rm -f %{buildroot}%{_libdir}/pkgconfig/glesv2.pc
rm -f %{buildroot}%{_libdir}/pkgconfig/xatracker.pc

#move real driver to libdir/driver
mkdir %{buildroot}%{_libdir}/driver
mv %{buildroot}%{_libdir}/libEGL* %{buildroot}%{_libdir}/driver/
mv %{buildroot}%{_libdir}/libGLES* %{buildroot}%{_libdir}/driver/

%post   -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post   -n libwayland-egl -p /sbin/ldconfig

%postun -n libwayland-egl -p /sbin/ldconfig

%files
%manifest %{name}.manifest
%defattr(-,root,root)
%license docs/COPYING
%config %{_sysconfdir}/drirc
%{_libdir}/dri
%{_libdir}/driver/libEGL.so
%{_libdir}/driver/libEGL.so.1*
%ifarch %ix86 x86_64
%{_libdir}/egl/egl_gallium.so
%endif
%_libdir/libxatracker.so
%_libdir/libxatracker.so.*
%{_libdir}/driver/libGLESv1_CM.so.1*
%{_libdir}/driver/libGLESv1_CM.so
%{_libdir}/driver/libGLESv2.so.2*
%{_libdir}/driver/libGLESv2.so
%{_libdir}/libgbm.so
%{_libdir}/libgbm.so.1*
%ifarch %ix86 x86_64
%{_libdir}/gbm/gbm_gallium_drm.so
%endif
%{_libdir}/libglapi.so
%{_libdir}/libglapi.so.0*


%if %{with wayland}
%files -n libwayland-egl
%manifest %{name}.manifest
%defattr(-,root,root)
%{_libdir}/libwayland-egl.so
%{_libdir}/libwayland-egl.so.1*

%files -n libwayland-egl-devel
%defattr(-,root,root)
%{_libdir}/pkgconfig/wayland-egl.pc
%endif

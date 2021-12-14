%define debug_package %{nil}

Name:           spice-toolkit_f
Version:        20170410
Release:        1%{?dist}
Summary:        Fortran SPICE Toolkit.

License:        NASA
Source0:        http://naif.jpl.nasa.gov/pub/naif/toolkit/FORTRAN/PC_Linux_gfortran_64bit/packages/toolkit.tar.Z

%description
%{summary}

%prep
%setup -q -n toolkit

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib
cp lib/spicelib.a %{buildroot}/usr/lib/libspice.a

%files
/usr/lib/libspice.a

%changelog
* Tue Dec 14 2021 Frédéric Pierret (fepitre) <frederic@invisiblethingslab.com> - 20170410-1
- Initial package.
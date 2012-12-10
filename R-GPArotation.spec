%global packname  GPArotation
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2010.07_1
Release:          1
Summary:          GPA Factor Rotation
Group:            Sciences/Mathematics
License:          GPL (>= 2) | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2010.07-1.tar.gz
BuildRequires:    R-devel
BuildRequires:    Rmath-devel
BuildRequires:    texlive-collection-latex
BuildRequires:    pkgconfig(lapack)

%description
Gradient Projection Algorithm Rotation for Factor Analysis. See
?GPArotation.Intro for more details.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/LICENSE
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help


%changelog
* Mon Feb 20 2012 Paulo Andrade <pcpa@mandriva.com.br> 2010.07_1-1
+ Revision: 777725
- Import R-GPArotation
- Import R-GPArotation


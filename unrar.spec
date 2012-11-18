Summary:	unRAR - extract, test and view RAR archives
Name:		unrar
Version:	4.2.4
Release:	1
License:	Freeware
Group:		Applications/Archiving
#Source0Download: http://www.rarlab.com/rar_add.htm
Source0:	http://www.rarlab.com/rar/%{name}src-%{version}.tar.gz
# Source0-md5:	8ea9d1b4139474b282d76e627a2de3e4
URL:		http://www.rarlab.com/
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		specflags	-fomit-frame-pointer

%description
The unRAR utility is a freeware program, distributed with source code
and developed for extracting, testing and viewing the contents of
archives created with the RAR archiver version 1.50 and above.

%prep
%setup -qn unrar

%build
%{__make} -f makefile.unix \
	CC="%{__cc}" \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcxxflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{man1,pl/man1}}

install unrar $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.txt
%attr(755,root,root) %{_bindir}/*


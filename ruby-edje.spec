Summary:	Ruby binding to the edje library
Summary(pl.UTF-8):   Dowiązania języka Ruby do biblioteki edje
Name:		ruby-edje
Version:	0
Release:	2
License:	Ruby's
Group:		Development/Languages
Source0:	%{name}.tar.gz
# Source0-md5:	63e27b8f8be6c377e57466bd495a71c1
URL:		http://code-monkey.de/projects/ruby-efl.html
BuildRequires:	edje-devel
BuildRequires:	rake
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby-devel
BuildRequires:	ruby-ecore-devel
%{?ruby_mod_ver_requires_eq}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby binding to the edje library.

%description -l pl.UTF-8
Dowiązania języka Ruby do biblioteki edje.

%prep
%setup -q -n %{name}

%build
rake

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_archdir},%{ruby_ridir}}

DESTDIR=$RPM_BUILD_ROOT RUBYARCHDIR=%{ruby_archdir} rake install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{ruby_archdir}/*.so

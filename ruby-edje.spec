%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define	ruby_ridir	%(ruby -r rbconfig -e 'include Config; print File.join(CONFIG["datadir"], "ri", CONFIG["ruby_version"], "system")')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	Ruby binding to the edje library
Name:		ruby-edje
Version:	0
Release:	1
License:	Ruby's
Group:		Development/Languages
Source0:	ruby-edje.tar.gz
# Source0-md5:	63e27b8f8be6c377e57466bd495a71c1
URL:		http://code-monkey.de/projects/ruby-efl.html
BuildRequires:	rake
BuildRequires:	ruby
BuildRequires:	ruby-devel
BuildRequires:	edje-devel
Requires:	ruby
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby binding to the Evas library.

%if 0
%package devel
Summary: Header files for ruby-edje
Group:	Development/Libraries
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
Header files for ruby-edje.
%endif

%prep
%setup -q -n ruby-edje

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
%{ruby_archdir}/*.so

%if 0
%files devel
%{ruby_archdir}/edje
%endif

Summary:	Bouml reference manual
Name:		bouml-doc
Version:	4.2
Release:	%mkrel 1
License:	GPLv2+
Group:		Development/Other
URL:		http://bouml.free.fr
Source0:	http://bouml.free.fr/doc%{version}.tar.gz
Source1:	http://bouml.free.fr/doc%{version}_A4.pdf
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
BOUML is a free Unified Modeling Language (UML 2) tool box allowing you
to specify and generate code in C++, Java, Idl, Php and Python.
You can use it to create nearly all of UML diagrams.
BOUML can generate code from those diagrams in
C++, Java, IDL, PHP and Python, and can also reverse existing code.

Contains reference manual.

%prep
%setup -q -c %{name}-%{version}
%__cp %{SOURCE1} .

%build

%install
rm -rf %{buildroot}
%__install -d -m 755 %{buildroot}%{_docdir}/bouml-%{version}
%__mv doc %{buildroot}%{_docdir}/bouml-%{version}/html
%__mv *.pdf %{buildroot}%{_docdir}/bouml-%{version}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%dir %{_docdir}/bouml-%{version}
%{_docdir}/bouml-%{version}/*



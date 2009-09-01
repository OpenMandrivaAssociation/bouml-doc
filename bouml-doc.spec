Summary:	Bouml reference manual
Name:		bouml-doc
Version:	4.12.4
Release:	%mkrel 1
License:	GPLv2+
Group:		Development/Other
URL:		http://bouml.free.fr
Source0:	http://downloads.sourceforge.net/bouml/doc%{version}.tar.gz
Source1:	http://downloads.sourceforge.net/bouml/doc%{version}_A4.pdf
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
%__install -d -m 755 %{buildroot}%{_datadir}/%{name}/pdf
%__mv doc %{buildroot}%{_datadir}/%{name}/html
%__mv *.pdf %{buildroot}%{_datadir}/%{name}/pdf

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/%{name}

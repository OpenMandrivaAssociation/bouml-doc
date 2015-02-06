Summary:	Bouml reference manual
Name:		bouml-doc
Version:	4.21
Release:	2
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


%changelog
* Sat Jul 10 2010 Luc Menut <lmenut@mandriva.org> 4.21-1mdv2011.0
+ Revision: 550519
- update to 4.21

* Sun Mar 21 2010 Luc Menut <lmenut@mandriva.org> 4.19-1mdv2010.1
+ Revision: 526154
- update to 4.19

* Tue Jan 05 2010 Luc Menut <lmenut@mandriva.org> 4.17-1mdv2010.1
+ Revision: 486507
- update to version 4.17

* Tue Sep 01 2009 Luc Menut <lmenut@mandriva.org> 4.12.4-1mdv2010.0
+ Revision: 424053
- update to new version 4.12.4

* Wed Feb 18 2009 Nicolas Vigier <nvigier@mandriva.com> 4.9-1mdv2009.1
+ Revision: 342555
- update to version 4.9

* Thu Sep 11 2008 Frederik Himpe <fhimpe@mandriva.org> 4.5-1mdv2009.0
+ Revision: 283930
- Update to 4.5, thanks to Luc Menut for feedback on cooker list

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 4.3.2-4mdv2009.0
+ Revision: 266342
- rebuild early 2009.0 package (before pixel changes)

* Sun Jun 08 2008 Funda Wang <fwang@mandriva.org> 4.3.2-3mdv2009.0
+ Revision: 216915
- install help files into /usr/share/bouml-doc so it has its own directory

* Sun Jun 08 2008 Funda Wang <fwang@mandriva.org> 4.3.2-2mdv2009.0
+ Revision: 216880
- move doc files into non-versioned dir

* Sat Jun 07 2008 Funda Wang <fwang@mandriva.org> 4.3.2-1mdv2009.0
+ Revision: 216664
- New version 4.3.2

* Fri Mar 21 2008 Nicolas Vigier <nvigier@mandriva.com> 4.2-1mdv2008.1
+ Revision: 189358
- import bouml-doc


* Thu Mar 20 2008 Luc Menut <Luc.Menut@supagro.inra.fr> 4.2-1mdv2008.1
- initial bouml-doc


%define		_lang		ku
Summary:	Kurdish resources for Iceweasel
Summary(pl.UTF-8):	Kurdyjskie pliki językowe dla Iceweasela
Name:		iceweasel-lang-%{_lang}
Version:	3.5.4
Release:	1
License:	MPL 1.1 or GPL v2+ or LGPL v2.1+
Group:		I18n
Source0:	http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/%{version}/linux-i686/xpi/%{_lang}.xpi
# Source0-md5:	06810c1007d5833274ca8daaa60874e1
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
BuildRequires:	zip
Requires:	iceweasel >= %{version}
Provides:	iceweasel-lang-resources = %{version}
Obsoletes:	mozilla-firefox-lang-ku
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_iceweaseldir	%{_datadir}/iceweasel
%define		_chromedir	%{_iceweaseldir}/chrome

%description
Kurdish resources for Iceweasel.

%description -l pl.UTF-8
Kurdyjskie pliki językowe dla Iceweasela.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_chromedir},%{_iceweaseldir}/defaults/profile}

unzip %{SOURCE0} -d $RPM_BUILD_ROOT%{_libdir}
mv -f $RPM_BUILD_ROOT%{_libdir}/chrome/* $RPM_BUILD_ROOT%{_chromedir}
sed -e 's@chrome/%{_lang}\.jar@%{_lang}.jar@' $RPM_BUILD_ROOT%{_libdir}/chrome.manifest \
	> $RPM_BUILD_ROOT%{_chromedir}/%{_lang}.manifest
mv -f $RPM_BUILD_ROOT%{_libdir}/*.rdf $RPM_BUILD_ROOT%{_iceweaseldir}/defaults/profile
# rebrand locale for iceweasel
cd $RPM_BUILD_ROOT%{_chromedir}
unzip ku.jar locale/branding/brand.dtd locale/branding/brand.properties \
	locale/browser/appstrings.properties
sed -i -e 's/Mozilla Firefox/Iceweasel/g; s/Firefox/Iceweasel/g;' \
	locale/branding/brand.dtd locale/branding/brand.properties
sed -i -e 's/Firefox/Iceweasel/g;' locale/browser/appstrings.properties
zip -0 ku.jar locale/branding/brand.dtd locale/branding/brand.properties \
	locale/browser/appstrings.properties
rm -f locale/branding/brand.dtd locale/branding/brand.properties \
	locale/browser/appstrings.properties

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_lang}.jar
%{_chromedir}/%{_lang}.manifest
# file conflict:
#%{_iceweaseldir}/defaults/profile/*.rdf

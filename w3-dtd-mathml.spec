Summary:	MathML 2.0 DTD (Document Type Definition)
Summary(pl):	DTD (definicja typu dokumentu) MathML 2.0
Name:		w3-dtd-mathml
Version:	2.0
Release:	1
License:	Free
Group:		Applications/Publishing/XML
URL:		http://www.w3.org/Math/
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	ad414900eda811fa96493802640f5648
BuildRequires:	rpm-build >= 4.0.2-94
BuildRequires:	/usr/bin/xmlcatalog
PreReq:		libxml2
Requires(post,preun):	/usr/bin/xmlcatalog
Requires:	libxml2-progs >= 2.4.17-6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define dtd_path	%{_datadir}/xml/w3c-mathml-dtd-%{version}
%define	xmlcat_file	%{dtd_path}/catalog.xml

%description
MathML 2.0 DTD (Document Type Definition).

%description -l pl
DTD (Document Type Definition, czyli definicja typu dokumentu) dla
MathML 2.0.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{dtd_path}

install *.{dtd,ent,mod} $RPM_BUILD_ROOT%{dtd_path}

%xmlcat_create $RPM_BUILD_ROOT%{xmlcat_file}

%xmlcat_add_rewrite \
	http://www.w3.org/TR/MathML2/dtd \
	file://%{dtd_path} \
	$RPM_BUILD_ROOT%{xmlcat_file}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if ! grep -q %{xmlcat_file} /etc/xml/catalog ; then
    %xmlcat_add %{xmlcat_file}

fi

%preun
if [ "$1" = "0" ] ; then
    %xmlcat_del %{xmlcat_file}

fi

%files
%defattr(644,root,root,755)
%{dtd_path}

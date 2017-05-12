#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : weave
Version  : 1.9.5
Release  : 1
URL      : https://github.com/weaveworks/weave/archive/v1.9.5.tar.gz
Source0  : https://github.com/weaveworks/weave/archive/v1.9.5.tar.gz
Source1  : https://github.com/Sirupsen/logrus/archive/4b6ea7319e214d98c938f12692336f7ca9348d6b.tar.gz
Source2  : https://github.com/boltdb/bolt/archive/c6ba97b89e0454fec9aa92e1d33a4e2c5fc1f631.tar.gz
Source3  : https://github.com/containernetworking/cni/archive/4ce9b019aab51b28a32ff6549784a69f9b209fe4.tar.gz
Source4  : https://github.com/coreos/go-iptables/archive/fbb73372b87f6e89951c2b6b31470c2c9d5cfae3.tar.gz
Source5  : https://github.com/docker/docker/archive/092cba3727bb9b4a2f0e922cd6c0f93ea270e363.tar.gz
Source6  : https://github.com/docker/go-units/archive/0dadbb0345b35ec7ef35e228dabb8de89a65bf52.tar.gz
Source7  : https://github.com/docker/libnetwork/archive/1861587d0fe7cdf85b89160ed36f20b81e96528d.tar.gz
Source8  : https://github.com/fsouza/go-dockerclient/archive/364c822d280c4f34afc3339e50d4fc0129d6b5ec.tar.gz
Source9  : https://github.com/golang/crypto/archive/7b428712abe956d0e9e1e9a01e163fb6c7171438.tar.gz
Source10  : https://github.com/golang/net/archive/d379faa25cbdc04d653984913a2ceb43b0bc46d7.tar.gz
Source11  : https://github.com/golang/sys/archive/62bee037599929a6e9146f29d10dd5208c43507d.tar.gz
Source12  : https://github.com/gorilla/context/archive/1ea25387ff6f684839d82767c1733ff4d4d15d0a.tar.gz
Source13  : https://github.com/gorilla/mux/archive/0eeaf8392f5b04950925b8a69fe70f110fa7cbfc.tar.gz
Source14  : https://github.com/hashicorp/go-cleanhttp/archive/ad28ea4487f05916463e2423a55166280e8254b5.tar.gz
Source15  : https://github.com/j-keck/arping/archive/af9a9003cfd88231902ab8959023d743f4ea93d7.tar.gz
Source16  : https://github.com/vishvananda/netlink/archive/c19091b1c6fb954a80f9f67abed2e2d780bb485b.tar.gz
Source17  : https://github.com/vishvananda/netns/archive/1fec6582c067519857603311ad090e23a5ca57de.tar.gz
Source18  : https://github.com/weaveworks/go-odp/archive/429cc5809b78f5627a2d220c1eaacaae3517226e.tar.gz
Source19  : https://github.com/weaveworks/mesh/archive/9a3824558758fb39a0e34f9aa6baa179fba8e3bc.tar.gz
Summary  : The open-source application container engine
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause CC-BY-SA-4.0 GPL-2.0 ISC LGPL-3.0 MIT MPL-2.0-no-copyleft-exception WTFPL
Requires: weave-bin
BuildRequires : go
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-don-t-build-in-container.patch
Patch2: 0002-hack-gopath-makefile.patch

%description
Docker is an open source project to build, ship and run any application as a
lightweight container.

Docker containers are both hardware-agnostic and platform-agnostic. This means
they can run anywhere, from your laptop to the largest EC2 compute instance and
everything in between - and they don't require you to use a particular
language, framework or packaging system. That makes them great building blocks
for deploying and scaling web apps, databases, and backend services without
depending on a particular stack or provider.

%package bin
Summary: bin components for the weave package.
Group: Binaries

%description bin
bin components for the weave package.


%prep
tar -xf %{SOURCE11}
tar -xf %{SOURCE1}
tar -xf %{SOURCE2}
tar -xf %{SOURCE3}
tar -xf %{SOURCE5}
tar -xf %{SOURCE8}
tar -xf %{SOURCE15}
tar -xf %{SOURCE16}
tar -xf %{SOURCE17}
tar -xf %{SOURCE10}
tar -xf %{SOURCE7}
tar -xf %{SOURCE19}
tar -xf %{SOURCE13}
tar -xf %{SOURCE14}
tar -xf %{SOURCE12}
tar -xf %{SOURCE18}
tar -xf %{SOURCE6}
tar -xf %{SOURCE9}
tar -xf %{SOURCE4}
cd ..
%setup -q -n weave-1.9.5
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/golang.org/x/sys
mv %{_topdir}/BUILD/sys-62bee037599929a6e9146f29d10dd5208c43507d/* %{_topdir}/BUILD/weave-1.9.5/src/golang.org/x/sys
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/Sirupsen/logrus
mv %{_topdir}/BUILD/logrus-4b6ea7319e214d98c938f12692336f7ca9348d6b/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/Sirupsen/logrus
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/boltdb/bolt
mv %{_topdir}/BUILD/bolt-c6ba97b89e0454fec9aa92e1d33a4e2c5fc1f631/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/boltdb/bolt
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/containernetworking/cni
mv %{_topdir}/BUILD/cni-4ce9b019aab51b28a32ff6549784a69f9b209fe4/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/containernetworking/cni
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/docker/docker
mv %{_topdir}/BUILD/moby-092cba3727bb9b4a2f0e922cd6c0f93ea270e363/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/docker/docker
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/fsouza/go-dockerclient
mv %{_topdir}/BUILD/go-dockerclient-364c822d280c4f34afc3339e50d4fc0129d6b5ec/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/fsouza/go-dockerclient
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/j-keck/arping
mv %{_topdir}/BUILD/arping-af9a9003cfd88231902ab8959023d743f4ea93d7/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/j-keck/arping
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/vishvananda/netlink
mv %{_topdir}/BUILD/netlink-c19091b1c6fb954a80f9f67abed2e2d780bb485b/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/vishvananda/netlink
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/vishvananda/netns
mv %{_topdir}/BUILD/netns-1fec6582c067519857603311ad090e23a5ca57de/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/vishvananda/netns
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/golang.org/x/net/
mv %{_topdir}/BUILD/net-d379faa25cbdc04d653984913a2ceb43b0bc46d7/* %{_topdir}/BUILD/weave-1.9.5/src/golang.org/x/net/
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/docker/libnetwork
mv %{_topdir}/BUILD/libnetwork-1861587d0fe7cdf85b89160ed36f20b81e96528d/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/docker/libnetwork
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/weaveworks/mesh
mv %{_topdir}/BUILD/mesh-9a3824558758fb39a0e34f9aa6baa179fba8e3bc/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/weaveworks/mesh
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/gorilla/mux
mv %{_topdir}/BUILD/mux-0eeaf8392f5b04950925b8a69fe70f110fa7cbfc/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/gorilla/mux
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/hashicorp/go-cleanhttp
mv %{_topdir}/BUILD/go-cleanhttp-ad28ea4487f05916463e2423a55166280e8254b5/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/hashicorp/go-cleanhttp
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/gorilla/context
mv %{_topdir}/BUILD/context-1ea25387ff6f684839d82767c1733ff4d4d15d0a/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/gorilla/context
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/weaveworks/go-odp/
mv %{_topdir}/BUILD/go-odp-429cc5809b78f5627a2d220c1eaacaae3517226e/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/weaveworks/go-odp/
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/docker/go-units
mv %{_topdir}/BUILD/go-units-0dadbb0345b35ec7ef35e228dabb8de89a65bf52/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/docker/go-units
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/golang.org/x/crypto
mv %{_topdir}/BUILD/crypto-7b428712abe956d0e9e1e9a01e163fb6c7171438/* %{_topdir}/BUILD/weave-1.9.5/src/golang.org/x/crypto
mkdir -p %{_topdir}/BUILD/weave-1.9.5/src/github.com/coreos/go-iptables
mv %{_topdir}/BUILD/go-iptables-fbb73372b87f6e89951c2b6b31470c2c9d5cfae3/* %{_topdir}/BUILD/weave-1.9.5/src/github.com/coreos/go-iptables
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1494604334
make V=1  %{?_smp_mflags} prog/weaveutil/weaveutil

%install
export SOURCE_DATE_EPOCH=1494604334
rm -rf %{buildroot}
%make_install
## make_install_append content
install -d -m 755 %{buildroot}/usr/libexec/cni
install -p -m 755 prog/weaveutil/weaveutil %{buildroot}/usr/libexec/cni/weave-plugin-%{version}
ln -sf ./weave-plugin-%{version} %{buildroot}/usr/libexec/cni/weave-ipam
ln -sf ./weave-plugin-%{version} %{buildroot}/usr/libexec/cni/weave-net
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/libexec/cni/weave-ipam
/usr/libexec/cni/weave-net
/usr/libexec/cni/weave-plugin-1.9.5
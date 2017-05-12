PKG_NAME := weave
URL := https://github.com/weaveworks/weave/archive/v1.9.5.tar.gz
ARCHIVES := https://github.com/golang/sys/archive/62bee037599929a6e9146f29d10dd5208c43507d.tar.gz src/golang.org/x/sys \
	https://github.com/Sirupsen/logrus/archive/4b6ea7319e214d98c938f12692336f7ca9348d6b.tar.gz src/github.com/Sirupsen/logrus \
	https://github.com/boltdb/bolt/archive/c6ba97b89e0454fec9aa92e1d33a4e2c5fc1f631.tar.gz src/github.com/boltdb/bolt \
	https://github.com/containernetworking/cni/archive/4ce9b019aab51b28a32ff6549784a69f9b209fe4.tar.gz src/github.com/containernetworking/cni \
	https://github.com/docker/docker/archive/092cba3727bb9b4a2f0e922cd6c0f93ea270e363.tar.gz src/github.com/docker/docker \
	https://github.com/fsouza/go-dockerclient/archive/364c822d280c4f34afc3339e50d4fc0129d6b5ec.tar.gz src/github.com/fsouza/go-dockerclient \
	https://github.com/j-keck/arping/archive/af9a9003cfd88231902ab8959023d743f4ea93d7.tar.gz src/github.com/j-keck/arping \
	https://github.com/vishvananda/netlink/archive/c19091b1c6fb954a80f9f67abed2e2d780bb485b.tar.gz src/github.com/vishvananda/netlink \
	https://github.com/vishvananda/netns/archive/1fec6582c067519857603311ad090e23a5ca57de.tar.gz src/github.com/vishvananda/netns \
	https://github.com/golang/net/archive/d379faa25cbdc04d653984913a2ceb43b0bc46d7.tar.gz src/golang.org/x/net/ \
	https://github.com/docker/libnetwork/archive/1861587d0fe7cdf85b89160ed36f20b81e96528d.tar.gz src/github.com/docker/libnetwork \
	https://github.com/weaveworks/mesh/archive/9a3824558758fb39a0e34f9aa6baa179fba8e3bc.tar.gz src/github.com/weaveworks/mesh \
	https://github.com/gorilla/mux/archive/0eeaf8392f5b04950925b8a69fe70f110fa7cbfc.tar.gz src/github.com/gorilla/mux \
	https://github.com/hashicorp/go-cleanhttp/archive/ad28ea4487f05916463e2423a55166280e8254b5.tar.gz src/github.com/hashicorp/go-cleanhttp \
	https://github.com/gorilla/context/archive/1ea25387ff6f684839d82767c1733ff4d4d15d0a.tar.gz src/github.com/gorilla/context \
	https://github.com/weaveworks/go-odp/archive/429cc5809b78f5627a2d220c1eaacaae3517226e.tar.gz src/github.com/weaveworks/go-odp/ \
	https://github.com/docker/go-units/archive/0dadbb0345b35ec7ef35e228dabb8de89a65bf52.tar.gz src/github.com/docker/go-units \
	https://github.com/golang/crypto/archive/7b428712abe956d0e9e1e9a01e163fb6c7171438.tar.gz src/golang.org/x/crypto \
	https://github.com/coreos/go-iptables/archive/fbb73372b87f6e89951c2b6b31470c2c9d5cfae3.tar.gz src/github.com/coreos/go-iptables

include ../common/Makefile.common

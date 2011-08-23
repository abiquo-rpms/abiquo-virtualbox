Name:     abiquo-virtualbox
Version:  1.8
Release:  2%{?dist} 
Summary:  Abiquo VirtualBox Cloud Node setup package
Group:    Development/System 
License:  Multiple 
URL:      http://www.abiquo.com 
#Source0:  README
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Requires: abiquo-cloud-node
Requires: VirtualBox-4.0
Requires: kernel-headers
Requires: kernel-devel
Requires: gcc
Requires: abiquo-aim
Requires: abiquo-cloud-node
Requires: bridge-utils
Requires: vconfig
Requires: make
Requires: avahi
BuildArch: noarch

%description
Next Generation Cloud Management Solution

This package prepares the host to work as a VirtualBox Cloud Node.

%post
# save current configs
cp %{_sysconfdir}/libvirt/libvirtd.conf %{_sysconfdir}/libvirt/libvirtd.conf.rpmsave
cp %{_sysconfdir}/sysconfig/libvirtd %{_sysconfdir}/sysconfig/libvirtd.rpmsave

cat > /etc/libvirt/libvirtd.conf <<EOF
listen_tls = 0
listen_tcp = 0
tcp_port = "16509"
#unix_sock_group = "libvirt"
#unix_sock_ro_perms = "0777"
#unix_sock_rw_perms = "0770"
#unix_sock_dir = "/var/run/libvirt"
auth_unix_ro = "none"
auth_unix_rw = "none"
auth_tcp = "none"
auth_tls = "none"
log_level = 3
log_outputs="3:syslog:libvirtd"

EOF

cat > /etc/sysconfig/libvirtd <<EOF
#LIBVIRTD_ARGS="--listen"
EOF

if [ -f /etc/default/virtualbox ]; then
  cp /etc/default/virtualbox /etc/default/virtualbox.rpmsave
fi
cat > /etc/default/virtualbox <<EOF
VBOXWEB_USER=root
VBoxManage setproperty websrvauthlibrary null
VBOXWEB_TIMEOUT=0
VBOXWEB_HOST=0.0.0.0
EOF

%files
%defattr(-,root,root,-)

%changelog
* Mon May 30 2011 Sergio Rubio <srubio@abiquo.com> - 1.8-1
- updated to 1.8

* Thu Mar 17 2011 Sergio Rubio <srubio@abiquo.com> - 1.7.5-1
- version bump

* Thu Jan 20 2011 Sergio Rubio srubio@abiquo.com 1.7-1
- Initial Release

Summary:	The default startup script for the X Window System
Name:		xinitrc
Version:	2.4.21
Release:	26
License:	Public Domain
Group:		System/X11
URL:		%{disturl}
Source0:	gdm.conf
Source1:	GiveConsole
Source3:	TakeConsole
Source4:	x11-Xresources
Source5:	Xaccess
Source6:	xdm.conf
Source7:	xdm-config
Source8:	xdm-Xsession
Source9:	xinitrc-fixkeyboard
Source11:	xinitrc-RunWM
Source12:	xinitrc-Xclients
Source13:	xinitrc-XIM
Source14:	xinitrc-xinitrc
Source15:	xinitrc-Xmodmap
Source16:	Xresources
Source17:	Xservers
Source18:	Xsession
Source19:	Xsetup_0
Source20:	Xwilling
Source21:	xdm-Xstartup
Source22:	xdm-Xreset
Source23:	XIM.xinit
Requires:	x11-server-xorg
# Because of <basedir>/X11 directory handling
Requires:	x11-server-common >= 1.4.2
Requires:	xdpyinfo
Requires:	xmodmap
Requires:	xsetroot
Requires:	/bin/sh
Requires:	/bin/grep
Requires:	sessreg
Requires:	xrdb
Requires:	xli
Suggests:	s2u
Conflicts:	initscripts < 6.87-2mdk
Conflicts:	gdm < 2.8.0.0
Conflicts:	xdm < 1.1.8
BuildArch:	noarch

%description
The xinitrc package contains the xinitrc file, a script which is used
to configure your X Window System session or to start a window manager.

%prep

%build
echo "Hello, i'm a build section"

%install

R=%{buildroot}
mkdir -p $R%{_sysconfdir}/X11/{xdm,xinit}
install -m755 %{SOURCE18} $R%{_sysconfdir}/X11/
install -m644 %{SOURCE4} $R%{_sysconfdir}/X11/Xresources

mkdir $R%{_sysconfdir}/X11/{xinit,xsetup}.d
install -m 755 %{SOURCE23} $R%{_sysconfdir}/X11/xinit.d/02XIM
mkdir $R%{_sysconfdir}/X11/wmsession.d
mkdir -p $R%{_datadir}/X11/xdm
install -m755 {%{SOURCE20},%{SOURCE19},%{SOURCE3},%{SOURCE1}} $R%{_datadir}/X11/xdm
ln -s ../../..%{_datadir}/X11/xdm/{Xwilling,Xsetup_0,TakeConsole,GiveConsole} $R%{_sysconfdir}/X11/xdm
install -m644 %{SOURCE7} %{SOURCE17} %{SOURCE16} %{SOURCE5} $R%{_sysconfdir}/X11/xdm
ln -s ../../../..%{_sysconfdir}/X11/xdm/{xdm-config,Xservers,Xresources,Xaccess} $R%{_datadir}/X11/xdm
install -m755 %{SOURCE8} $R%{_datadir}/X11/xdm/Xsession

install -m755 %{SOURCE22} $R%{_datadir}/X11/xdm/Xreset
install -m755 %{SOURCE21} $R%{_datadir}/X11/xdm/Xstartup
ln -s ../../..%{_datadir}/X11/xdm/{Xsession,Xreset,Xstartup} $R%{_sysconfdir}/X11/xdm

install -m644 %{SOURCE15} $R%{_sysconfdir}/X11/Xmodmap
install -m644 %{SOURCE14} $R%{_sysconfdir}/X11/xinit/xinitrc
install -m644 %{SOURCE12} $R%{_sysconfdir}/X11/xinit/Xclients
install -m644 %{SOURCE9} $R%{_sysconfdir}/X11/xinit/fixkeyboard
install -m644 %{SOURCE13} $R%{_sysconfdir}/X11/xinit/XIM

mkdir -p $R%{_bindir}/
install -m755 %{SOURCE11} $R%{_bindir}/RunWM
for i in Fvwm95 MWM AfterStep WindowMaker; do ln -sf RunWM $R%{_bindir}/RunWM.$i;done

mkdir -p $R%{_datadir}/X11/dm.d
install -m644 %{SOURCE0} $R%{_datadir}/X11/dm.d/20gdm.conf
install -m644 %{SOURCE6} $R%{_datadir}/X11/dm.d/30xdm.conf

%files
%config(noreplace) %{_sysconfdir}/X11/Xmodmap
%config(noreplace) %{_sysconfdir}/X11/Xresources
%config(noreplace) %{_sysconfdir}/X11/xdm/xdm-config
%config(noreplace) %{_sysconfdir}/X11/xdm/Xservers
%config(noreplace) %{_sysconfdir}/X11/xdm/Xresources
%config(noreplace) %{_sysconfdir}/X11/xdm/Xaccess

%{_sysconfdir}/X11/xdm/GiveConsole
%{_sysconfdir}/X11/xdm/TakeConsole
%{_sysconfdir}/X11/xdm/Xreset
%{_sysconfdir}/X11/xdm/Xsession
%{_sysconfdir}/X11/xdm/Xsetup_0
%{_sysconfdir}/X11/xdm/Xstartup
%{_sysconfdir}/X11/xdm/Xwilling


%dir %{_sysconfdir}/X11/wmsession.d
%dir %{_sysconfdir}/X11/xinit
%dir %{_sysconfdir}/X11/xinit.d
%dir %{_sysconfdir}/X11/xsetup.d
%{_sysconfdir}/X11/Xsession
%{_sysconfdir}/X11/xinit.d/02XIM
%{_sysconfdir}/X11/xinit/XIM
%{_sysconfdir}/X11/xinit/Xclients
%{_sysconfdir}/X11/xinit/fixkeyboard
%{_sysconfdir}/X11/xinit/xinitrc
%{_bindir}/*
%{_datadir}/X11/dm.d
%{_datadir}/X11/xdm

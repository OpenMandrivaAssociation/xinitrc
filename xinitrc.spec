%define name    xinitrc
%define version 2.4.19
%define release %mkrel 14

Summary:	The default startup script for the X Window System
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://www.mandrivalinux.com/

Source0: 	gdm.conf
Source1: 	GiveConsole
Source2: 	kdm.conf
Source3: 	TakeConsole
Source4: 	x11-Xresources
Source5: 	Xaccess
Source6: 	xdm.conf
Source7: 	xdm-config
Source8: 	xdm-Xsession
Source9: 	xinitrc-fixkeyboard
Source10: 	xinitrc-Mod_Meta_L_Disable
Source11: 	xinitrc-RunWM
Source12: 	xinitrc-Xclients
Source13: 	xinitrc-XIM
Source14: 	xinitrc-xinitrc
Source15: 	xinitrc-Xmodmap
Source16: 	Xresources
Source17: 	Xservers
Source18: 	Xsession
Source19: 	Xsetup_0
Source20: 	Xwilling
Source21: 	xdm-Xstartup
Source22: 	xdm-Xreset
Source23:	XIM.xinit
Source24: 	kdm3.conf

License:	Public Domain
Group:		System/X11
Buildroot:	%{_tmppath}/%{name}-%{version}-root
Requires:	x11-server-xorg
# Because of <basedir>/X11 directory handling
Requires:	x11-server-common >= 1.4.2
Requires:	xdpyinfo
Requires:	xmodmap
Requires:	xsetroot
Requires:	/bin/sh
Requires: 	/bin/grep
Requires: 	sessreg
Requires:   	xrdb
Conflicts:	initscripts < 6.87-2mdk
Conflicts:	gdm < 2.8.0.0
Conflicts:	xdm < 1.1.8
BuildArchitectures:	noarch

%description
The xinitrc package contains the xinitrc file, a script which is used
to configure your X Window System session or to start a window manager.

%prep


%install
rm -rf $RPM_BUILD_ROOT

R=$RPM_BUILD_ROOT/
S=%{_sourcedir}
	
mkdir -p $R%{_sysconfdir}/X11/{xdm,xinit}
install -m755 $S/Xsession $R%{_sysconfdir}/X11/
install -m644 $S/x11-Xresources $R%{_sysconfdir}/X11/Xresources

mkdir $R%{_sysconfdir}/X11/{xinit,xsetup}.d
install -m 755 $S/xinitrc-Mod_Meta_L_Disable $R%{_sysconfdir}/X11/xinit.d/Mod_Meta_L_Disable
install -m 755 $S/XIM.xinit $R%{_sysconfdir}/X11/xinit.d/02XIM
mkdir $R%{_sysconfdir}/X11/wmsession.d
mkdir -p $R%{_datadir}/X11/xdm
install -m755 $S/Xwilling $S/Xsetup_0 $S/TakeConsole $S/GiveConsole $R%{_datadir}/X11/xdm
install -m644 $S/{xdm-config,Xservers,Xresources,Xaccess} $R%{_sysconfdir}/X11/xdm
ln -s ../../../..%{_sysconfdir}/X11/xdm/{xdm-config,Xservers,Xresources,Xaccess} $R%{_datadir}/X11/xdm
install -m755 $S/xdm-Xsession $R%{_datadir}/X11/xdm/Xsession

install -m755 $S/xdm-Xreset $R%{_datadir}/X11/xdm/Xreset
install -m755 $S/xdm-Xstartup $R%{_datadir}/X11/xdm/Xstartup

install -m644 $S/xinitrc-Xmodmap $R%{_sysconfdir}/X11/Xmodmap
for i in xinitrc Xclients fixkeyboard XIM; do install -m755 $S/xinitrc-$i $R%{_sysconfdir}/X11/xinit/$i;done

mkdir -p $R%{_bindir}/
install -m755 $S/xinitrc-RunWM $R%{_bindir}/RunWM
for i in Fvwm95 MWM AfterStep WindowMaker; do ln -sf RunWM $R%{_bindir}/RunWM.$i;done

mkdir -p $R%{_datadir}/X11/dm.d
install -m644 $S/kdm.conf $R%{_datadir}/X11/dm.d/10kdm.conf
install -m644 $S/kdm3.conf $R%{_datadir}/X11/dm.d/15kdm3.conf
install -m644 $S/gdm.conf $R%{_datadir}/X11/dm.d/20gdm.conf
install -m644 $S/xdm.conf $R%{_datadir}/X11/dm.d/30xdm.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/X11/Xmodmap
%config(noreplace) %{_sysconfdir}/X11/Xresources
%config(noreplace) %{_sysconfdir}/X11/xdm/*
%dir %{_sysconfdir}/X11/wmsession.d
%dir %{_sysconfdir}/X11/xdm
%dir %{_sysconfdir}/X11/xinit
%dir %{_sysconfdir}/X11/xinit.d
%dir %{_sysconfdir}/X11/xsetup.d
%{_sysconfdir}/X11/Xsession
%{_sysconfdir}/X11/xinit.d/Mod_Meta_L_Disable
%{_sysconfdir}/X11/xinit.d/02XIM
%{_sysconfdir}/X11/xinit/XIM
%{_sysconfdir}/X11/xinit/Xclients
%{_sysconfdir}/X11/xinit/fixkeyboard
%{_sysconfdir}/X11/xinit/xinitrc
%{_bindir}/*
%{_datadir}/X11/dm.d
%{_datadir}/X11/xdm

ó
¦^c           @   sV  d  d l  Z  d  d l Z d  d l Z d   Z d   Z d   Z d   Z d   Z e d k rRd  d l  Z  g  Z	 g  Z
 e Z xÔe sNe  j d  d	 j e e e	    Z e GHe d
  Z e d k rxe	 D]- Z d j e  GHd  d l Z e j d  qÐ Wq~ e d k r§e d  Z e e	 k r0d GHn  e e	 k re d  Z e e
 k r\d GHn  e e
 k rre   n  e d  Z e d k re   q¤e Z qKe   q~ e d k rDe e d   Z e	 j e  e såe d  n  e rKe d  Z e
 j e  e se d  n  e rAd GHd  d l Z e j d  qAqKq~ e   q~ Wn  d S(   iÿÿÿÿNc          C   sÂ  t  j d  d GHd GHd GHd GHd GHt d  }  |  d k rH t   nv|  d k r· t d  } | sp t   n  | d	 j |  k rª t   t  j d
 j |   d GHq¾t j   n|  d k r#t d  } | sß t   n  | d	 j |  k rt   t  j d j |   d GHq¾t   n |  d k rRt  j d  } t d  t	   nl |  d k r·t d  } | szt   n  | d	 j |  k r¾t
   t  j d j |   d GHq¾n t   d  S(   Nt   clears   	      =====================s   	      |    Termux-Bot     |t    s/   	Ketik [4m/help[0m untuk menampilkan bantuan
s   	> s   /helps   /installs   {}s   pkg install {} -y &> /dev/nulls   
	> Installing Done!s   /clones   git clone {} &> /dev/nulls   
	> Cloned Done!s   /sees   pkg list-installeds   
Press enter for backs
   /uninstalls    pkg uninstall {} -y &> /dev/nulls   
	> Uninstalled Done!(   t   ost   systemt	   raw_inputt	   menu_helpt   exitt   formatt   tikt   syst   tokt   bott   kon(   t   polt   packt   clonet   at   unins(    (    s   termux-bot.pyR      sP    






c          C   s3   t  j d  d GHd d  l }  t d  t   d  S(   NR    sf  
Notes :

for install package in termux you can use command
[4m/install and enter[0m. then [4minput the package name.[0m
and for clone a github can use command [4m/clone and enter[0m. Then [4minput the URL
github.[0m

[4m/see[0m for see package installed and [4m/uninstall and enter[0m, then
enter the [4mpackage name[0m for installed.

Thanks
iÿÿÿÿs   Press enter for back(   R   R   t   timeR   R   (   R   (    (    s   termux-bot.pyR   8   s
    
c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   	> Install starting i   (   R	   t   stdoutt   flushR   t   sleep(   t   titikt   o(    (    s   termux-bot.pyR   J   s
      c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   	> Clone starting i   (   R	   R   R   R   R   (   t   tiktokt   i(    (    s   termux-bot.pyR
   O   s
      c          C   sF   d d d g }  x0 |  D]( } d | Gt  j j   t j d  q Wd  S(   Ns   .   s   ..  s   ... s   	> Uninstall starting i   (   R	   R   R   R   R   (   t   tikont   k(    (    s   termux-bot.pyR   T   s
      t   __main__R    sJ   
	   TERMUX-BOT LOGIN

	[1] Member Terdaftar ({})
	[2] Login
	[3] Daftar 
s   	> t   1s   - {}i   t   2s   
Username: s3   [!]Username tidak tersedia, silahkan [4mDaftar[0ms
   Password: s   [!]Password salahs   

	> Ulang? t   yt   3s   [!]Masukkan usernames   [!]Masukkan kata sandis   [!]Akun berhasil dibuat(   R   R	   R   R   R   R   R
   R   t   __name__t   membert   sandit   Falset   stopR   R   t   strt   lent   menuR   t   pilt   khazR   t   usert   passwdt   nanyat   TrueR   t   sett   appendt   setpass(    (    (    s   termux-bot.pyt   <module>   sh   	3					

	

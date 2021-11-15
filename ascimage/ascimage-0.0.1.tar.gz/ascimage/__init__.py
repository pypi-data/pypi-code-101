import numpy as np
import itertools
import shutil

__version__="0.0.1"

def _rgb2clrcode(bgr):
	d=1
	t=16
	h=16
	for c in bgr:
		c=max(min(c,255),0)
		q=((c*2+0x33)//0x66)
		u=c-(q-1)*0x33
		u=(u*4+0x33)//0x66-2
		h+=d*(q+u)
		t+=d*q
		d*=6
	return t,h

def _rgb2str(rgb,subrgb):
	b,h=_rgb2clrcode(rgb[::-1])
	if subrgb is not None:
		sb,_=_rgb2clrcode(subrgb[0][::-1])
		sh,_=_rgb2clrcode(subrgb[1][::-1])
	else:
		sb=b
		sh=h
	return "\x1b[48;5;%dm\x1b[38;5;%dmX\x1b[48;5;%dm\x1b[38;5;%dmX"%(sb,sh,b,h)

_defaultMaxSize=256
def setDefaultMaxSize(newMaxSize):
	_defaultMaxSize=newMaxSize

def makeImageStr(imHWC,targetsizeWH=None,valrange=None,zoomxy=None):
	def getInbound(xy,wh,ofs=0):
		res=[0,0]
		for i in range(2):
			res[ i ]=min(max(xy[ i ],0),wh[ i ]+ofs)
		return res
		
	imarrHWC=imHWC
	tgsizeWH=targetsizeWH
	normrng=valrange
	# fix shape of input array if needed.
	if len(imarrHWC.shape)==1:
		imarrHWC=imarrHWC.reshape(1,imarrHWC.shape[0],1)
	if len(imarrHWC.shape)==2:
		imarrHWC=imarrHWC.reshape(list(imarrHWC.shape)+[1])
	hwc=list(imarrHWC.shape)

	if zoomxy is not None:
		if not isinstance(zoomxy,(list,tuple)):
			zoomxy=[zoomxy,0,0]
		elif len(zoomxy)==1:
			zoomxy=[zoomxy[0],0,0]
		elif len(zoomxy)==2:
			zoomxy=[zoomxy,0,0]
		elif len(zoomxy)==4:
			zoomxy=[zoomxy[0:2]]+list(zoomxy[2:])
		if isinstance(zoomxy[0],(tuple,list)):
			twh,x,y=zoomxy
			LT=twh[0]+x,twh[1]+y
			RB=LT[0]+twh[0],LT[1]+twh[1]
			LT=getInbound(LT,hwc[:2][::-1])
			RB=getInbound(RB,hwc[:2][::-1])
			zoomxy=None
			if RB[0]-LT[0]<=0 or RB[1]<=LT[1]:
				return "\x1b[0m\n"
			imarrHWC=imarrHWC[LT[1]:RB[1],LT[0]:RB[0]]
	hwc=list(imarrHWC.shape)
	# calc effective tgsize
	conWH=list(shutil.get_terminal_size())
	conWH[1]-=4
	if tgsizeWH is None:
		tgsizeWH=1
	if not isinstance(tgsizeWH,(tuple,list)):
		tgsizeWH=[tgsizeWH,tgsizeWH]
	ref=[0,0]
	for i in range(2):
		tga=abs(tgsizeWH[ i ])
		if tga<=1.0 and tga>0:
			ref[ i ]=conWH[ i ]*tga/(2-i)
		elif tgsizeWH[ i ]<=0:
			ref[ i ]=conWH[ i ]+tgsizeWH[ i ]
		else:
			ref[ i ]=tgsizeWH[ i ]
		if ref[ i ]>=_defaultMaxSize:
			ref[ i ]=_defaultMaxSize
	tgsizeWH=ref
	# align aspect ratio.
	px=1.0*hwc[1]/tgsizeWH[0]
	py=1.0*hwc[0]/tgsizeWH[1]
	p=max(px,py,1)
	tgwh =[int(hwc[1]/p),int(hwc[0]/p)]
	if zoomxy is not None:
		mz=hwc[1]/tgwh[0]
		z,ox,oy=zoomxy
		if z<1 or z>=mz:
			twh=tgwh
		else:
			twh=[int(hwc[1]/z),int(hwc[0]/z)]
		ltrb=[[0,0],[0,0]]
		ox=min(max(ox,-hwc[1]//2),hwc[1]//2)
		oy=min(max(oy,-hwc[0]//2),hwc[0]//2)
		for i,o in enumerate((ox,oy)):
			ltrb[0][i]=(hwc[1-i]-twh[i])//2+o
			ltrb[1][i]=ltrb[0][i]+twh[i]
		im=np.zeros(list(twh[::-1])+[imHWC.shape[2]],dtype=imarrHWC.dtype)
		destltrb=[0,0,0,0]
		for ixy in range(2):
			if ltrb[0][ixy]<0:
				destltrb[ixy]=-ltrb[0][ixy]
				ltrb[0][ixy]=0
			else:
				destltrb[ixy]=0
			if ltrb[1][ixy]>hwc[1-ixy]:
				ltrb[1][ixy]=hwc[1-ixy]
			destltrb[ixy+2]=ltrb[1][ixy]-ltrb[0][ixy]+destltrb[ixy]
		print(destltrb,ltrb)
		im[destltrb[1]:destltrb[3],destltrb[0]:destltrb[2]]=imHWC[ltrb[0][1]:ltrb[1][1],ltrb[0][0]:ltrb[1][0]]
		imarrHWC=im
		hwc=list(imarrHWC.shape)

	# range setting.
	if imarrHWC.dtype==np.uint8 and normrng is  None:
		normrng=(0,255)
	elif normrng is None:
		normrng=(np.min(imarrHWC),np.max(imarrHWC))
	if normrng[1]==normrng[0]:
		normrng=(normrng[0],normrng[0]+1)
	imarrHWC=np.clip((imarrHWC.astype(np.float32)-normrng[0])/(normrng[1]-normrng[0])*255,0,255).astype(np.uint8)
	
	# let's make ascii-art!
	s=""
	patchT=0
	clrs=np.array([[255,0,255],[0,255,0],[255,0,0],[0,0,255],[255,255,0],[0,255,255],[255,255,255]])
	s+="\x1b[0m"+("*"*tgwh[0])+"\n"
	for iY in range(tgwh[1]):
		patchB=hwc[0]*(iY+1)//tgwh[1]
		patchL=0
		for iX in range(tgwh[0]):
			patchR=hwc[1]*(iX+1)//tgwh[0]
			partimg=imarrHWC[patchT:patchB,patchL:patchR]
			mc=np.mean(partimg,axis=(0,1))
			# check gray-scale:
			if hwc[2]==1:
				mc=[mc,mc,mc]
			sub=[mc,mc]
			b=0
			for cc in clrs:
				if len(np.where((partimg[:,:,0]==cc[0]) & (partimg[:,:,1]==cc[1]) & (partimg[:,:,2]==cc[2]))[0])>=4:
					sub[b]=cc
					b+=1
				if b==2:
					break
			s+=_rgb2str(mc,sub)
			patchL=patchR
		s+="\x1b[0m\n"
		patchT=patchB
		
	s+="\x1b[0m"+("*"*tgwh[0])+"\n"
	return s

def imprint(imHWC,targetsizeWH=None,valrange=None,zoomxy=None):
	print(makeImageStr(imHWC,targetsizeWH,valrange,zoomxy))
	

def _drawColorPatch(targetsizeWH=None,zoomxy=None):
	u=np.array(list(itertools.product(range(0,256),range(0,200)))).reshape((256,200,2)).transpose(1,0,2)
	u=np.concatenate((u,128+u[:,:,0:1]//2-u[:,:,1:2]//2),axis=2)
	print(u.shape)
	imprint(u,targetsizeWH=targetsizeWH,valrange=(0,255),zoomxy=zoomxy)

def imprint_cmd():
	import sys
	import argparse
	from PIL import Image
	arg=argparse.ArgumentParser()
	arg.add_argument("imgfile",type=str)
	arg.add_argument("--outsize","-s",type=int,nargs=2)
	arg.add_argument("--zoomxy","-z",type=float,nargs=3)
	#cfg=arg.parse_args(["../../../DCIM/001/DSC_0643.JPG","-z","1","0","0"])
	#cfg=arg.parse_args(["__test","-s","12","12","-z","1","0","0"])
	cfg=arg.parse_args()
	if cfg.zoomxy is None:
		zoomxy=None
	else:
		zoomxy=[cfg.zoomxy[0],int(cfg.zoomxy[1]),int(cfg.zoomxy[2])]
	kwargs={"targetsizeWH": cfg.outsize,"zoomxy": zoomxy}
	if cfg.imgfile=="__test":
		_drawColorPatch(**kwargs)
	else:
		jpg=np.array(Image.open(cfg.imgfile))
		imprint(jpg,**kwargs)

if __name__=="__main__":
	imprint_cmd()



all: 
	sox hack-intro.wav -c 1 -C 8.9 fw.mp3
	lzma fw.mp3
	mksquashfs root root.img -all-root
	cat fw.mp3.lzma root.img final.txt > fw.img
	mkimage -A arm -C lzma -n "VCS Company dschleede@gmail.com" -d fw.img fw.uboot
	rm -rf fw.img root.img fw.mp3.lzma
	mv fw.uboot fw.img

CHEM_HOME=/Users/rgrout/Code/rev-controlled/LBNL/Combustion/Chemistry
#CHEM_HOME=/home/marc/src/CCSE/Combustion/Chemistry
BIN = ${CHEM_HOME}/tools/chemkin/bin
DATA = ${CHEM_HOME}/data/chem-H

# Pick mechanism by setting relevant filenames


# -------- chem-H
CHEMFILE=chem-H.inp
THERMFILE=thermo12.dat
TRANFILE=transport12.dat

# -------- LiDryerMOD  (ie, LiDryer with the species order switched to match chem-H)
#CHEMFILE=LiDryerMOD.mec
#THERMFILE=LiDryer.therm
#TRANFILE=LiDryer.trans


# Set names for executables
CKINTERP=ckinterp.exe
TRANFIT=tranfit.exe
PREMIX=premix.exe

all: premix premix_new

premix:
	gfortran premix.f prdriv.f twopnt.f refine.f cktime.f tranlib_d.f math.f mach.f cklib_d.f -o premix_repo

premix_new:
	gcc -I. -std=c99 -c BurkeDryer.c
	#gfortran  premix_new.f prdriv.f twopnt.f refine.f cktime.f tranlib_d.f math.f mach.f misc_math.f chem-H.o -o premix_new 
	gfortran  premix_new.f prdriv.f twopnt.f refine.f cktime.f tranlib_d.f math.f mach.f  BurkeDryer.o cklib_d.f -o premix_new 

clean:
	rm -f *.asc *.bak *.bin *.dat *.out *.o premix_stock premix_new

tranlink: ${DATA}/${TRANFILE}
	\rm -rf tran.dat
	ln -s ${DATA}/${TRANFILE} tran.dat

thermlink: ${DATA}/${THERMFILE}
	\rm -rf therm.dat
	ln -s ${DATA}/${THERMFILE} therm.dat

chem.out: ${BIN}/${CKINTERP} thermlink ${DATA}/${CHEMFILE}
	${BIN}/${CKINTERP} < ${DATA}/${CHEMFILE} > chem.out

tran.out: chem.out ${BIN}/${TRANFIT} tranlink
	${BIN}/${TRANFIT} > tran.out

stock: premix tran.out chem.out thermlink tranlink 
	./premix_stock < premix.inp #> premix.out

new: tran.out chem.out thermlink tranlink premix_new
	./premix_new < premix.inp #> premix.out

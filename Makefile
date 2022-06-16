DEBUG ?= 0
NCCL ?=0
NCCLCMMD = -D_USE_NCCL -lnccl
ARCH= -gencode=arch=compute_61,code=sm_61 -gencode=arch=compute_75,code=sm_75

ifeq ($(DEBUG), 0)
ifeq ($(NCCL),0)
simple2DFD_rls: simple2DFD.cu
	nvcc -O2 ./simple2DFD.cu $(ARCH)  -I./ -o ./build/$@
else 
simple2DFD_rls_nccl: simple2DFD.cu
	nvcc -O2 ./simple2DFD.cu $(ARCH)  $(NCCLCMMD) -I./ -o ./build/$@
	@echo Useing nccl now!
endif
else
ifeq ($(NCCL),0)
simple2DFD_dbg: simple2DFD.cu
	nvcc -g -G ./simple2DFD.cu $(ARCH)  -I./ -o ./build/$@
else
simple2DFD_dbg_nccl: simple2DFD.cu
	nvcc -g -G ./simple2DFD.cu $(ARCH)  $(NCCLCMMD)  -I./ -o ./build/$@
	@echo Useing nccl now!
endif
endif

clean:
	rm -f ./build/simple2DFD_*


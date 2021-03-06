# **********************************************************************
# * $Id: Makefile.in
# *
# * PostGIS - Spatial Types for PostgreSQL
# * http://postgis.refractions.net
# * Copyright 2008 Paul Ramsey, Mark Cave-Ayland
# *
# * This is free software; you can redistribute and/or modify it under
# * the terms of the GNU General Public Licence. See the COPYING file.
# *
# **********************************************************************

CC=gcc
CFLAGS=-g -O2  -Wall -Wmissing-prototypes

CUNIT_LDFLAGS=
CUNIT_CPPFLAGS= -I..

# GTK includes and libraries
GTK_CFLAGS =  
GTK_LIBS =  
GTK_WIN32_FLAGS = 

# PostgreSQL frontend CPPFLAGS and LDFLAGS (for compiling and linking with libpq)
PGSQL_FE_CPPFLAGS=-I/usr/include
PGSQL_FE_LDFLAGS=-L/usr/lib64 -lpq

# liblwgeom
LIBLWGEOM=../../liblwgeom/.libs/liblwgeom.a

# iconv flags
ICONV_LDFLAGS= -lc
ICONV_CFLAGS=

# GetText includes and libraries
GETTEXT_CFLAGS = 
GETTEXT_LDFLAGS =  

# Build full linking line
LDFLAGS = -lm $(GETTEXT_LDFLAGS) $(PGSQL_FE_LDFLAGS) $(ICONV_LDFLAGS) $(CUNIT_LDFLAGS)

# Object files
OBJS=	\
	cu_pgsql2shp.o \
	cu_shp2pgsql.o \
	cu_tester.o

LOADER_OBJS= \
	../dbfopen.o \
	../shpopen.o \
	../getopt.o \
	../shpcommon.o \
	../safileio.o \
	../pgsql2shp-core.o \
	../shp2pgsql-core.o

# If we couldn't find the cunit library then display a helpful message
ifeq ($(CUNIT_LDFLAGS),)
all: requirements_not_met_cunit
check: requirements_not_met_cunit
else

$(LOADER_OBJS):
	make -C ..

# Build the unit tester
all: cu_tester

# Build and run the unit tester
check: cu_tester
	@./cu_tester

endif

# Build the main unit test executable
cu_tester: $(LOADER_OBJS) $(OBJS) 
	$(CC)  $^ -o $@ $(LIBLWGEOM) $(LDFLAGS)

# Command to build each of the .o files
$(OBJS): %.o: %.c
	$(CC) $(CFLAGS) $(CUNIT_CPPFLAGS) $(GTK_CFLAGS) $(PGSQL_FE_CPPFLAGS) -c -o $@ $<

# Clean target
clean:
	rm -f $(OBJS)
	rm -f cu_tester.exe

distclean: clean
	rm -f Makefile

# Requirements message
requirements_not_met_cunit:
	@echo
	@echo "WARNING:"
	@echo
	@echo "configure was unable to find CUnit which is required for unit testing."
	@echo "In order to enable unit testing, you must install CUnit and then re-run configure."
	@echo

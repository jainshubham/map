#############################################################################
# $Id$
#
# Copyright (c) 2011 Regents of the University of California
#   <bkpark@ucdavis.edu>
# Copyright (c) 2009 Sandro Santilli <strk@keybit.net>
#
# This is free software; you can redistribute and/or modify it under
# the terms of the GNU General Public Licence. See the COPYING file.
#
#############################################################################

# Set CFLAGS afer PGXS, otherwise it will get overwritten with the PGXS
# version which is not what we want. 
CC=gcc
CFLAGS=-g -O2  -fPIC -DPIC  -Wall -Wmissing-prototypes 
top_builddir = ../..
SHELL = /bin/sh
INSTALL = $(SHELL) ../../install-sh
LIBTOOL = $(SHELL) $(top_builddir)/libtool

# Filenames with extension as determined by the OS
RASTER2PGSQL=raster2pgsql

# PostgreSQL executable directory
PGSQL_BINDIR=/usr/bin

# PostgreSQL frontend CPPFLAGS and LDFLAGS (for compiling and linking with libpq)
PGSQL_FE_CPPFLAGS=-I/usr/include
PGSQL_FE_LDFLAGS=-L/usr/lib64 -lpq

RT_CORE=../rt_core

LIBLWGEOM_LDFLAGS=../../liblwgeom/liblwgeom.la
LIBLWGEOM_CFLAGS=-I../../liblwgeom
LIBGDAL_CFLAGS=-I/usr/include/gdal
LIBGDAL_LDFLAGS=-L/usr/lib64 -lgdal
PROJ_CFLAGS=
GEOS_CFLAGS=-I/usr/include
GEOS_LDFLAGS=-L/usr/lib64 -lgeos_c

RTCORE_CFLAGS=-I$(RT_CORE)
RTCORE_LDFLAGS=$(RT_CORE)/librtcore.a

# GetText includes and libraries
GETTEXT_CFLAGS = 
GETTEXT_LDFLAGS =  

# iconv flags
ICONV_LDFLAGS= -lc
ICONV_CFLAGS=

CFLAGS = \
	-g -O2  -fPIC -DPIC  -Wall -Wmissing-prototypes \
	$(RTCORE_CFLAGS) \
	$(LIBLWGEOM_CFLAGS) \
	$(PROJ_CFLAGS) \
	$(PGSQL_FE_CPPFLAGS) \
	$(LIBGDAL_CFLAGS) \
	$(GEOS_CFLAGS) \
	$(GETTEXT_CFLAGS) \
	$(ICONV_CFLAGS)

LDFLAGS = \
	 \
	$(RTCORE_LDFLAGS) \
	$(LIBLWGEOM_LDFLAGS) \
	$(PGSQL_FE_LDFLAGS) \
	$(LIBGDAL_LDFLAGS) \
	$(GEOS_LDFLAGS) \
	$(GETTEXT_LDFLAGS) \
	$(ICONV_LDFLAGS) \
	-lm

all: $(RASTER2PGSQL)

raster2pgsql.o: raster2pgsql.c
	$(CC) $(CFLAGS) -c $<

$(RASTER2PGSQL): raster2pgsql.o $(RT_CORE)/librtcore.a
	$(LIBTOOL) --mode=link $(CC) $(CFLAGS) $^ $(LDFLAGS) -o $@

installdir:
	@mkdir -p $(DESTDIR)$(PGSQL_BINDIR)

install: installdir
	$(LIBTOOL) --mode=install $(INSTALL) $(RASTER2PGSQL) "$(DESTDIR)$(PGSQL_BINDIR)/$(RASTER2PGSQL)"

uninstall:
	$(LIBTOOL) --mode=uninstall $(RM) "$(DESTDIR)$(PGSQL_BINDIR)/$(RASTER2PGSQL)"

$(RT_CORE)/librtcore.a:
	$(MAKE) -C ../rt_core

clean:
	rm -rf .libs
	rm -f *.o $(RASTER2PGSQL)

distclean: clean
	rm -f Makefile

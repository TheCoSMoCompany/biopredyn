cmake_minimum_required(VERSION 2.6)
project(libsbmlsim)

set(LIBSBMLSIM_SOURCE_DIR ${CMAKE_CURRENT_SOURCE_DIR})

# cmake variables
if(MSVC)
  add_definitions(/W3)
else(MSVC)
  #  add_definitions(-Wall -Wextra -ansi -pedantic -fno-strict-aliasing)
  add_definitions(-Wall -Wextra -fno-strict-aliasing)
endif(MSVC)
# BioPreDyn patch - not overwriting global CMAKE_C_FLAGS settings anymore
set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -O2")

# build mode
if(NOT CMAKE_BUILD_TYPE)
  set(CMAKE_BUILD_TYPE Release CACHE STRING
    "Choose the type of build, options are: None Debug Release RelWithDebInfo MinSizeRel."
    FORCE)
endif(NOT CMAKE_BUILD_TYPE)

# language bindings - BioPreDyn patch: removed unused language wrapping options
option(WITH_PYTHON   "Generate Python language bindings." OFF)

# - Try to find libSBML
# Once done this will define
#  LIBSBML_FOUND - System has libSBML
#  LIBSBML_INCLUDE_DIRS - The libSBML include directories
#  LIBSBML_LIBRARIES - The libraries needed to use libSBML
#  LIBSBML_DEFINITIONS - Compiler switches required for using libSBML
# BioPreDyn patch - Removed search for LIBSBML_LIBRARY and LIBSBML_INCLUDE_DIR
# and LIBSBML_DEFINITIONS determination

find_library(LIBBZIP2_LIBRARY
  NAMES bzip2.lib bz2 libbz2.lib
  PATHS /usr/lib /usr/local/lib /opt/local/lib
        ${CMAKE_SOURCE_DIR}/depend/lib
  HINTS ${PC_LIBBZIP2} ${PC_LIBBZIP2_LIBRARY_DIRS} )

set(LIBSBML_LIBRARIES ${LIBSBML_LIBRARY} ${LIBBZIP2_LIBRARY} )
set(LIBSBML_INCLUDE_DIRS ${LIBSBML_INCLUDE_DIR} )

add_subdirectory(src)

message(STATUS "
----------------------------------------------------------------------
libSBMLSim version ${PACKAGE_VERSION}
----------------------------------------------------------------------

Configured on host "$ENV{COMPUTERNAME}" ${HOSTNAME}
  host type                     = ${CMAKE_SYSTEM_NAME}
  host operating system         = ${CMAKE_SYSTEM_NAME} ${CMAKE_SYSTEM_VERSION}
  host CPU architecture         = ${CMAKE_SYSTEM_PROCESSOR}

General build flags:
  CC                            = ${CMAKE_C_COMPILER}
  CXX                           = ${CMAKE_CXX_COMPILER}
  CPPFLAGS                      = ${BUILD_DEFINITIONS}
  CFLAGS                        = ${CMAKE_C_FLAGS}
  CXXFLAGS                      = ${CMAKE_CXX_FLAGS}
  LDFLAGS                       = ${CMAKE_EXE_LINKER_FLAGS}

SBML parser library configuration:
  SBML library                   = ${LIBSBML_LIBRARY}
  CPPFLAGS for SBML              = -I${LIBSBML_INCLUDE_DIR}
  LIBS for SBML                  = ${LIBSBML_LIBRARY}

Other libSBMLSim configuration settings:
  Installation $prefix          = ${CMAKE_INSTALL_PREFIX}")


# This file will be configured to contain variables for CPack. These variables
# should be set in the CMake list file of the project before CPack module is
# included. The list of available CPACK_xxx variables and their associated
# documentation may be obtained using
#  cpack --help-variable-list
#
# Some variables are common to all generators (e.g. CPACK_PACKAGE_NAME)
# and some are specific to a generator
# (e.g. CPACK_NSIS_EXTRA_INSTALL_COMMANDS). The generator specific variables
# usually begin with CPACK_<GENNAME>_xxxx.


SET(CPACK_BINARY_BUNDLE "")
SET(CPACK_BINARY_CYGWIN "")
SET(CPACK_BINARY_DEB "")
SET(CPACK_BINARY_DRAGNDROP "")
SET(CPACK_BINARY_NSIS "")
SET(CPACK_BINARY_OSXX11 "")
SET(CPACK_BINARY_PACKAGEMAKER "")
SET(CPACK_BINARY_RPM "")
SET(CPACK_BINARY_STGZ "")
SET(CPACK_BINARY_TBZ2 "")
SET(CPACK_BINARY_TGZ "")
SET(CPACK_BINARY_TZ "")
SET(CPACK_BINARY_WIX "")
SET(CPACK_BINARY_ZIP "")
SET(CPACK_CMAKE_GENERATOR "Unix Makefiles")
SET(CPACK_COMPONENT_UNSPECIFIED_HIDDEN "TRUE")
SET(CPACK_COMPONENT_UNSPECIFIED_REQUIRED "TRUE")
SET(CPACK_DEBIAN_PACKAGE_ARCHITECTURE "i386")
SET(CPACK_DEBIAN_PACKAGE_PRIORITY "optional")
SET(CPACK_DEBIAN_PACKAGE_SECTION "Libraries")
SET(CPACK_GENERATOR "TGZ;ZIP")
SET(CPACK_IGNORE_FILES "/CVS/;/\\.svn/;/\\.git/;\\.DS_Store;\\.swp$;/build/;^bindings/java;^bindings/perl;^bindings/python;/diff/;/simulation_results/;testcases/simulateSBML;testcases/cases/;testcases/.*-results\\.csv;testcases/out\\.csv;build_csharp\\.sh;build_java\\.sh;build_python\\.sh;depend-.*\\.zip;result\\.zip;Makefile\\.dist;ev_func_piece\\.xml;00remove\\.sh")
SET(CPACK_INSTALLED_DIRECTORIES "/home/bertrand/Soft/libsbmlsim-1.1.0;/")
SET(CPACK_INSTALL_CMAKE_PROJECTS "")
SET(CPACK_INSTALL_PREFIX "/usr")
SET(CPACK_MODULE_PATH "")
SET(CPACK_NSIS_DISPLAY_NAME "libsbmlsim 1.1.0")
SET(CPACK_NSIS_INSTALLER_ICON_CODE "")
SET(CPACK_NSIS_INSTALLER_MUI_ICON_CODE "")
SET(CPACK_NSIS_INSTALL_ROOT "$PROGRAMFILES")
SET(CPACK_NSIS_PACKAGE_NAME "libsbmlsim 1.1.0")
SET(CPACK_OUTPUT_CONFIG_FILE "/home/bertrand/Soft/libsbmlsim-1.1.0/build/CPackConfig.cmake")
SET(CPACK_PACKAGE_CONTACT "LibSBMLSim development Team <sbmlsim@fun.bio.keio.ac.jp>")
SET(CPACK_PACKAGE_DEFAULT_LOCATION "/")
SET(CPACK_PACKAGE_DESCRIPTION "LibSBMLSim")
SET(CPACK_PACKAGE_DESCRIPTION_FILE "/home/bertrand/Soft/libsbmlsim-1.1.0/README.txt")
SET(CPACK_PACKAGE_DESCRIPTION_SUMMARY "LibSBMLSim: The library for simulating SBML models")
SET(CPACK_PACKAGE_FILE_NAME "libsbmlsim-1.1.0")
SET(CPACK_PACKAGE_INSTALL_DIRECTORY "libsbmlsim 1.1.0")
SET(CPACK_PACKAGE_INSTALL_REGISTRY_KEY "libsbmlsim 1.1.0")
SET(CPACK_PACKAGE_NAME "libsbmlsim")
SET(CPACK_PACKAGE_NAME_LOWERCASE "libsbmlsim")
SET(CPACK_PACKAGE_RELOCATABLE "true")
SET(CPACK_PACKAGE_VENDOR "LibSBMLSim development team")
SET(CPACK_PACKAGE_VERSION "1.1.0")
SET(CPACK_PACKAGE_VERSION_MAJOR "1")
SET(CPACK_PACKAGE_VERSION_MINOR "1")
SET(CPACK_PACKAGE_VERSION_PATCH "0")
SET(CPACK_RESOURCE_FILE_LICENSE "/home/bertrand/Soft/libsbmlsim-1.1.0/LICENSE.txt")
SET(CPACK_RESOURCE_FILE_README "/home/bertrand/Soft/libsbmlsim-1.1.0/README.txt")
SET(CPACK_RESOURCE_FILE_WELCOME "/home/bertrand/Soft/libsbmlsim-1.1.0/templates/Welcome.txt")
SET(CPACK_RPM_PACKAGE_ARCHITECTURE "i386")
SET(CPACK_RPM_PACKAGE_GROUP "Libraries/Development")
SET(CPACK_RPM_PACKAGE_LICENSE "LGPL")
SET(CPACK_SET_DESTDIR "ON")
SET(CPACK_SOURCE_CYGWIN "")
SET(CPACK_SOURCE_GENERATOR "TGZ;ZIP")
SET(CPACK_SOURCE_IGNORE_FILES "/CVS/;/\\.svn/;/\\.git/;\\.DS_Store;\\.swp$;/build/;^bindings/java;^bindings/perl;^bindings/python;/diff/;/simulation_results/;testcases/simulateSBML;testcases/cases/;testcases/.*-results\\.csv;testcases/out\\.csv;build_csharp\\.sh;build_java\\.sh;build_python\\.sh;depend-.*\\.zip;result\\.zip;Makefile\\.dist;ev_func_piece\\.xml;00remove\\.sh")
SET(CPACK_SOURCE_INSTALLED_DIRECTORIES "/home/bertrand/Soft/libsbmlsim-1.1.0;/")
SET(CPACK_SOURCE_OUTPUT_CONFIG_FILE "/home/bertrand/Soft/libsbmlsim-1.1.0/build/CPackSourceConfig.cmake")
SET(CPACK_SOURCE_PACKAGE_FILE_NAME "libsbmlsim-1.1.0")
SET(CPACK_SOURCE_TBZ2 "")
SET(CPACK_SOURCE_TGZ "")
SET(CPACK_SOURCE_TOPLEVEL_TAG "Linux-Source")
SET(CPACK_SOURCE_TZ "")
SET(CPACK_SOURCE_ZIP "")
SET(CPACK_STRIP_FILES "")
SET(CPACK_SYSTEM_NAME "Linux")
SET(CPACK_TOPLEVEL_TAG "Linux-Source")
SET(CPACK_WIX_SIZEOF_VOID_P "4")
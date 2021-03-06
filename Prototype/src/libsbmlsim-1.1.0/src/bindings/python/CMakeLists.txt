# This is a CMake example for Python

cmake_minimum_required(VERSION 2.8)

FIND_PACKAGE(SWIG 2.0 REQUIRED)
INCLUDE(${SWIG_USE_FILE})

FIND_PACKAGE(PythonLibs)
INCLUDE_DIRECTORIES(${PYTHON_INCLUDE_PATH})
INCLUDE_DIRECTORIES(${CMAKE_CURRENT_SOURCE_DIR})
INCLUDE_DIRECTORIES(${LIBSBMLSIM_SOURCE_DIR}/src/libsbmlsim ${LIBSBML_INCLUDE_DIR})

SET(CMAKE_SWIG_FLAGS "")

SET_SOURCE_FILES_PROPERTIES(libsbmlsim.i PROPERTIES CPLUSPLUS OFF)
SET_SOURCE_FILES_PROPERTIES(libsbmlsim.i PROPERTIES SWIG_FLAGS "-includeall")
SWIG_ADD_MODULE(libsbmlsim python libsbmlsim.i ${SOURCES_LIB})
# BioPreDyn patch - linking libSBMLSim wrappers to libSBML wrappers
SWIG_LINK_LIBRARIES(libsbmlsim sbmlsim-static ${LIBSBML_LIBRARY} ${PYTHON_LIBRARIES})

# BioPreDyn patch - changed libSBMLSim install directory
INSTALL(TARGETS ${SWIG_MODULE_libsbmlsim_REAL_NAME} DESTINATION ${PYTHON_PACKAGE_INSTALL_DIR}/libsbmlsim )

file(WRITE "${CMAKE_CURRENT_BINARY_DIR}/libsbmlsim.pth" "libsbmlsim\n")
INSTALL(FILES ${CMAKE_CURRENT_BINARY_DIR}/libsbmlsim.pth  DESTINATION ${PYTHON_PACKAGE_INSTALL_DIR})
INSTALL(FILES ${CMAKE_CURRENT_BINARY_DIR}/libsbmlsim.py  DESTINATION ${PYTHON_PACKAGE_INSTALL_DIR}/libsbmlsim )

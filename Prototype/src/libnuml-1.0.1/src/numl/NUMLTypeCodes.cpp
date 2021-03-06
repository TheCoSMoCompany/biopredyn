/**
* Begin svn Header
* $Rev: 51 $:	Revision of last commit
* $Author: josephodada@gmail.com $:	Author of last commit
* $Date: 2013-12-04 17:29:20 +0100 (Wed, 04 Dec 2013) $:	Date of last commit
* $HeadURL: http://numl.googlecode.com/svn/trunk/libnuml/src/numl/NUMLTypeCodes.cpp $
* $Id: NUMLTypeCodes.cpp 51 2013-12-04 16:29:20Z josephodada@gmail.com $
* End svn Header
* ****************************************************************************
* This file is part of libNUML.  Please visit http://code.google.com/p/numl/for more
* information about NUML, and the latest version of libNUML.
* Copyright (c) 2013 The University of Manchester.
*
* This library is free software; you can redistribute it and/or modify it
* under the terms of the GNU Lesser General Public License as published
* by the Free Software Foundation.  A copy of the license agreement is
* provided in the file named "LICENSE.txt" included with this software
* distribution and also available online as http://www.gnu.org/licenses/lgpl.html
*
* Contributors:
* Joseph O. Dada, The University of Manchester - initial API and implementation
* ****************************************************************************
**/

#include <numl/common/common.h>
#include <numl/NUMLTypeCodes.h>

LIBNUML_CPP_NAMESPACE_BEGIN

static
const char* NUML_TYPE_CODE_STRINGS[] =
{
    "(Unknown NUML Type)"
  , "Document"
  , "OntologyTerms"
  , "OntologyTerm"
  , "ResultComponent"
  , "ResultComponents"
  , "Dimension"
  , "DimensionDescription"
  , "CompositeValue"
  , "CompositeValues"
  , "Tuple"
  , "Tuples"
  , "AtomicValue"
  , "AtomicValues"
  , "CompositeDescription"
  , "TupleDescription"
  , "AtomicDescription"
  , "NUMLList"
  , "Constraint"
};

/**
 * @return a human readable name for the given NUMLTypeCode_t.  The caller
 * does not own the returned string and is therefore not allowed to modify
 * it.
 */
LIBNUML_EXTERN
const char *
NUMLTypeCode_toString (NUMLTypeCode_t tc)
{
  return NUML_TYPE_CODE_STRINGS[tc];
}

LIBNUML_CPP_NAMESPACE_END

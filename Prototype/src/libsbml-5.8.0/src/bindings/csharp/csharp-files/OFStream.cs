/* ----------------------------------------------------------------------------
 * This file was automatically generated by SWIG (http://www.swig.org).
 * Version 2.0.6
 *
 * Do not make changes to this file unless you know what you are doing--modify
 * the SWIG interface file instead.
 * ----------------------------------------------------------------------------- */

namespace libsbmlcs {

using System;
using System.Runtime.InteropServices;

public class OFStream : OStream {
	private HandleRef swigCPtr;
	
	internal OFStream(IntPtr cPtr, bool cMemoryOwn) : base(libsbmlPINVOKE.OFStream_SWIGUpcast(cPtr), cMemoryOwn)
	{
		//super(libsbmlPINVOKE.OFStreamUpcast(cPtr), cMemoryOwn);
		swigCPtr = new HandleRef(this, cPtr);
	}
	
	internal static HandleRef getCPtr(OFStream obj)
	{
		return (obj == null) ? new HandleRef(null, IntPtr.Zero) : obj.swigCPtr;
	}
	
	internal static HandleRef getCPtrAndDisown (OFStream obj)
	{
		HandleRef ptr = new HandleRef(null, IntPtr.Zero);
		
		if (obj != null)
		{
			ptr             = obj.swigCPtr;
			obj.swigCMemOwn = false;
		}
		
		return ptr;
	}

  ~OFStream() {
    Dispose();
  }

  public override void Dispose() {
    lock(this) {
      if (swigCPtr.Handle != IntPtr.Zero) {
        if (swigCMemOwn) {
          swigCMemOwn = false;
          libsbmlPINVOKE.delete_OFStream(swigCPtr);
        }
        swigCPtr = new HandleRef(null, IntPtr.Zero);
      }
      GC.SuppressFinalize(this);
      base.Dispose();
    }
  }

  public OFStream(string filename, bool is_append) : this(libsbmlPINVOKE.new_OFStream__SWIG_0(filename, is_append), true) {
    if (libsbmlPINVOKE.SWIGPendingException.Pending) throw libsbmlPINVOKE.SWIGPendingException.Retrieve();
  }

  public OFStream(string filename) : this(libsbmlPINVOKE.new_OFStream__SWIG_1(filename), true) {
    if (libsbmlPINVOKE.SWIGPendingException.Pending) throw libsbmlPINVOKE.SWIGPendingException.Retrieve();
  }

  public void open(string filename, bool is_append) {
    libsbmlPINVOKE.OFStream_open__SWIG_0(swigCPtr, filename, is_append);
    if (libsbmlPINVOKE.SWIGPendingException.Pending) throw libsbmlPINVOKE.SWIGPendingException.Retrieve();
  }

  public void open(string filename) {
    libsbmlPINVOKE.OFStream_open__SWIG_1(swigCPtr, filename);
    if (libsbmlPINVOKE.SWIGPendingException.Pending) throw libsbmlPINVOKE.SWIGPendingException.Retrieve();
  }

  public void close() {
    libsbmlPINVOKE.OFStream_close(swigCPtr);
  }

  public bool is_open() {
    bool ret = libsbmlPINVOKE.OFStream_is_open(swigCPtr);
    return ret;
  }

}

}
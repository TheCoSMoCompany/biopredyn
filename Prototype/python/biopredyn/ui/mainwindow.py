#!/usr/bin/env python
# coding=utf-8

## @package biopredyn
## Copyright: [2012-2019] Cosmo Tech, All Rights Reserved
## License: BSD 3-Clause

from PySide.QtGui import *
from PySide.QtCore import *
import os
import project

## Class describing the main window for the BioPreDyn user interface.
# Derived from PySide.QtGui.QMainWindow.
class MainWindow(QMainWindow):
  ## @var menu_bar
  # Main menu bar of the BioPreDyn user interface.
  ## @var project
  # Central widget of 'self'.
  ## @var filename
  # Absolute path of the last file having been opened in 'self'.
  ## @var save_filename
  # Absolute path of the last file having been saved in 'self'.
  ## @var status_bar
  # A PySide.QtGui.QStatusBar object.

  ## Constructor.
  # @param self The object pointer.
  def __init__(self):
    QMainWindow.__init__(self, None)
    self.filename = None
    self.save_filename = None
    self.setWindowTitle("BioPreDyn UI")
    self.setWindowIcon(QIcon("icons/bpd.xpm"))
    self.setMinimumSize(800, 600)
    self.project = project.Project(self)
    # Menu bar
    self.menu_bar = QMenuBar(self)
    self.setMenuBar(self.menu_bar)
    # 'File' menu
    file_menu = QMenu("File", parent=self.menu_bar)
    new_wf_action = QAction("New", self) # connect to new_workflow
    new_wf_action.setShortcut(QKeySequence.New)
    new_wf_action.setStatusTip("Create a new empty work flow.")
    new_wf_action.triggered.connect(self.new_workflow)
    file_menu.addAction(new_wf_action)
    open_wf_action = QAction("Open", self) # connect to open_workflow
    open_wf_action.setShortcut(QKeySequence.Open)
    open_wf_action.setStatusTip("Open SED-ML work flows.")
    open_wf_action.triggered.connect(self.open_workflow)
    file_menu.addAction(open_wf_action)
    saveas_wf_action = QAction("Save as", self) # connect to save_workflow_as
    saveas_wf_action.setShortcut(QKeySequence.SaveAs)
    saveas_wf_action.setStatusTip("Save current work flow as.")
    saveas_wf_action.triggered.connect(self.save_workflow_as)
    file_menu.addAction(saveas_wf_action)
    save_wf_action = QAction("Save", self) # connect to save_workflow
    save_wf_action.setShortcut(QKeySequence.Save)
    save_wf_action.setStatusTip("Save current work flow.")
    save_wf_action.triggered.connect(self.save_workflow)
    file_menu.addAction(save_wf_action)
    close_wf_action = QAction("Close", self) # connect to close_workflow
    close_wf_action.setShortcut(QKeySequence.Close)
    close_wf_action.setStatusTip("Close current work flow.")
    close_wf_action.triggered.connect(self.close_workflow)
    file_menu.addAction(close_wf_action)
    file_menu.addSeparator()
    run_wf_action = QAction("Run", self) # connect to run_workflow
    run_wf_action.setShortcut("Ctrl+R")
    run_wf_action.setStatusTip("Run all the tasks of the current work flow, " +
      "and process all its outputs.")
    run_wf_action.triggered.connect(self.run_workflow)
    file_menu.addAction(run_wf_action)
    file_menu.addSeparator()
    quit_action = QAction("Quit", self) # connect to close
    quit_action.setShortcut(QKeySequence.Quit)
    quit_action.setStatusTip("Quit the BioPreDyn UI.")
    quit_action.triggered.connect(self.close)
    file_menu.addAction(quit_action)
    self.menu_bar.addMenu(file_menu)
    # 'Edit' menu
    edit_menu = QMenu("Edit", parent=self.menu_bar)
    edit_elt_action = QAction("Edit element", self) # connect to edit_element
    edit_elt_action.setShortcut("Ctrl+Shift+E")
    edit_elt_action.setStatusTip("Edit the attributes of the selected element.")
    edit_elt_action.triggered.connect(self.edit_element)
    edit_menu.addAction(edit_elt_action)
    self.menu_bar.addMenu(edit_menu)
    # Central widget
    self.setCentralWidget(self.project)
    # Status bar
    self.status_bar = QStatusBar(parent=self)
    self.setStatusBar(self.status_bar)

  ## Closes the active workflow.
  # @param self The object pointer.
  def close_workflow(self):
    self.project.remove_workflow()

  ## Opens a biopredyn.ui.DialogBox window providing several widgets for editing
  ## the current element.
  # @param self The object pointer.
  def edit_element(self):
    self.project.edit_element()

  ## Creates a new workflow.
  # @param self The object pointer.
  def new_workflow(self):
    self.project.new_workflow()

  ## Opens a workflow from a user-defined source file.
  # Opens a dialog window asking for the location of a SED-ML file; if a valid
  # SED-ML file location is provided by the user, it is opened.
  # @param self The object pointer.
  def open_workflow(self):
    dir = (os.path.dirname(self.filename)
      if self.filename is not None else ".")
    fname = QFileDialog.getOpenFileNames(
      self, "Open SED-ML file", dir, "XML files (*.xml)")
    if len(fname[0]) > 0:
      self.filename = fname[0][0]
      for f in fname[0]:
        self.project.add_workflow(f)

  ## Runs the active workflow.
  # @param self The object pointer.
  def run_workflow(self):
    self.project.run_workflow()

  ## Saves the active workflow to the location defined by its 'source'
  ## attribute.
  # @param self The object pointer.
  def save_workflow(self):
    self.project.write_workflow()

  ## Saves the active workflow to a user-defined location.
  # Opens a dialog window asking for the location of a SED-ML file; if a valid
  # SED-ML file location is provided by the user, it is opened.
  # @param self The object pointer.
  def save_workflow_as(self):
    dir = (os.path.dirname(self.save_filename)
      if self.save_filename is not None else ".")
    fname = QFileDialog.getSaveFileName(
      self, "Save SED-ML file", dir, "XML file (*.xml)")
    if len(fname[0]) > 0:
      self.save_filename = fname[0]
      self.project.write_workflow(source=self.save_filename)

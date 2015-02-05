#!/usr/bin/env python
# coding=utf-8

## @package biopredyn
## Copyright: [2012-2015] The CoSMo Company, All Rights Reserved
## License: BSD 3-Clause

import os
from PySide.QtGui import *

## Base class for SED-ML elements in parent
## biopredyn.ui.navigationtree.NavigationTree object. Derived from
## PySide.QtGui.QTreeWidgetItem.
class TreeElement(QTreeWidgetItem):

  ## Constructor.
  # @param self The object pointer.
  # @param parent A PySide.QtGui.QWidget object.
  def __init__(self, parent):
    QTreeWidgetItem.__init__(self, parent)

  ## Recursively browses the parents of 'self' until a
  ## biopredyn.ui.tree.WorkFlowElement is reached, then returns it.
  # @param self The object pointer.
  # @return The top-level biopredyn.ui.tree.WorkFlowElement parent of'self'.
  def get_workflow_element(self):
    return self.parent().get_workflow_element()

## TreeElement-derived class representing biopredyn.change.Change
## objects in parent biopredyn.ui.navigationtree.NavigationTree object.
class ChangeElement(TreeElement):
  # @var change
  # Reference to the biopredyn.change.Change object represented by this.

  ## Constructor.
  # @param self The object pointer.
  # @param change A biopredyn.change.Change object.
  # @param parent A TreeElement object.
  def __init__(self, change, parent):
    TreeElement.__init__(self, parent)
    self.change = change
    self.setText(0, self.change.get_name())
    self.setText(1, self.change.get_id())

## TreeElement-derived class representing biopredyn.signals.Data
## objects in parent biopredyn.ui.navigationtree.NavigationTree object.
class DataElement(TreeElement):
  # @var signal
  # Reference to the biopredyn.signals.Data object represented by this.

  ## Constructor.
  # @param self The object pointer.
  # @param signal A biopredyn.signals.Data object.
  # @param parent A TreeElement object.
  def __init__(self, signal, parent):
    TreeElement.__init__(self, parent)
    self.signal = signal
    self.setText(0, self.signal.get_name())
    self.setText(1, self.signal.get_id())

## TreeElement-derived class representing biopredyn.datagenerator.DataGenerator
## objects in parent biopredyn.ui.navigationtree.NavigationTree object.
class DataGeneratorElement(TreeElement):
  ## @var datagenerator
  # Reference to the biopredyn.datagenerator.DataGenerator object represented by
  # this.
  ## @var par_list
  # A biopredyn.ui.tree.TreeElement object for listing parameters. 
  ## @var var_list
  # A biopredyn.ui.tree.TreeElement object for listing variables.

  ## Constructor.
  # @param self The object pointer.
  # @param datagen A biopredyn.datagenerator.DataGenerator object.
  # @param parent A TreeElement object.
  def __init__(self, datagen, parent):
    TreeElement.__init__(self, parent)
    self.datagenerator = datagen
    self.setText(0, self.datagenerator.get_name())
    self.setText(1, self.datagenerator.get_id())
    # list of variables
    self.var_list = TreeElement(self)
    self.var_list.setText(0, 'listOfVariables')
    self.addChild(self.var_list)
    for v in datagen.get_variables():
      self.var_list.addChild(VariableElement(v, self.var_list))
    # list of parameters
    self.par_list = TreeElement(self)
    self.par_list.setText(0, 'listOfParameters')
    self.addChild(self.par_list)
    for p in datagen.get_parameters():
      self.par_list.addChild(ParameterElement(p, self.par_list))

## TreeElement-derived class representing biopredyn.model.Model
## objects in parent biopredyn.ui.navigationtree.NavigationTree object.
class ModelElement(TreeElement):
  ## @var change_list
  # A biopredyn.ui.tree.TreeElement object for listing changes.
  ## @var model
  # Reference to the biopredyn.model.Model object represented by this.

  ## Constructor.
  # @param self The object pointer.
  # @param model A biopredyn.model.Model object.
  # @param parent A TreeElement object.
  def __init__(self, model, parent):
    TreeElement.__init__(self, parent)
    self.model = model
    self.setText(0, self.model.get_name())
    self.setText(1, self.model.get_id())
    # list of changes
    self.change_list = TreeElement(self)
    self.change_list.setText(0, 'listOfChanges')
    self.addChild(self.change_list)
    for c in model.get_changes():
      self.change_list.addChild(ChangeElement(p, self.change_list))

## TreeElement-derived class representing biopredyn.output.Output
## objects in parent biopredyn.ui.navigationtree.NavigationTree object.
class OutputElement(TreeElement):
  ## @var data_list
  # A biopredyn.ui.tree.TreeElement object for listing data elements.
  ## @var output
  # Reference to the biopredyn.output.Output object represented by this.

  ## Constructor.
  # @param self The object pointer.
  # @param model A biopredyn.model.Model object.
  # @param parent A TreeElement object.
  def __init__(self, output, parent):
    TreeElement.__init__(self, parent)
    self.output = output
    self.setText(0, self.output.get_name())
    self.setText(1, self.output.get_id())
    # list of data elements
    name = 'listOfDataSets'
    if output.get_type() == 'plot2D':
      name = 'listOfCurves'
    elif output.get_type() == 'plot3D':
      name = 'listOfSurfaces'
    self.data_list = TreeElement(self)
    self.data_list.setText(0, name)
    self.addChild(self.data_list)
    for s in output.get_signals():
      self.data_list.addChild(DataElement(s, self.data_list))

## TreeElement-derived class representing biopredyn.parameter.Parameter
## objects in parent biopredyn.ui.navigationtree.NavigationTree object.
class ParameterElement(TreeElement):
  # @var parameter
  # Reference to the biopredyn.parameter.Parameter object represented by this.

  ## Constructor.
  # @param self The object pointer.
  # @param param A biopredyn.parameter.Parameter object.
  # @param parent A TreeElement object.
  def __init__(self, param, parent):
    TreeElement.__init__(self, parent)
    self.parameter = param
    self.setText(0, self.parameter.get_name())
    self.setText(1, self.parameter.get_id())

## TreeElement-derived class representing biopredyn.simulation.Simulation
## objects in parent biopredyn.ui.navigationtree.NavigationTree object.
class SimulationElement(TreeElement):
  # @var simulation
  # Reference to the biopredyn.simulation.Simulation object represented by this.

  ## Constructor.
  # @param self The object pointer.
  # @param task A biopredyn.simulation.Simulation object.
  # @param parent A TreeElement object.
  def __init__(self, simulation, parent):
    TreeElement.__init__(self, parent)
    self.simulation = simulation
    self.setText(0, self.simulation.get_name())
    self.setText(1, self.simulation.get_id())

## TreeElement-derived class representing biopredyn.task.Task
## objects in parent biopredyn.ui.navigationtree.NavigationTree object.
class TaskElement(TreeElement):
  # @var task
  # Reference to the biopredyn.task.Task object represented by this.

  ## Constructor.
  # @param self The object pointer.
  # @param task A biopredyn.task.Task object.
  # @param parent A TreeElement object.
  def __init__(self, task, parent):
    TreeElement.__init__(self, parent)
    self.task = task
    self.setText(0, self.task.get_name())
    self.setText(1, self.task.get_id())

## TreeElement-derived class representing biopredyn.variable.Variable
## objects in parent biopredyn.ui.navigationtree.NavigationTree object.
class VariableElement(TreeElement):
  # @var variable
  # Reference to the biopredyn.variable.Variable object represented by this.

  ## Constructor.
  # @param self The object pointer.
  # @param var A biopredyn.variable.Variable object.
  # @param parent A TreeElement object.
  def __init__(self, var, parent):
    TreeElement.__init__(self, parent)
    self.variable = var
    self.setText(0, self.variable.get_name())
    self.setText(1, self.variable.get_id())

## TreeElement-derived class representing biopredyn.workflow.WorkFlow objects in
## parent biopredyn.ui.navigationtree.NavigationTree object.
class WorkFlowElement(TreeElement):
  ## @var workflow
  # Reference to the biopredyn.workflow.WorkFlow object represented by self.
  ## @var sim_list
  # A biopredyn.ui.tree.TreeElement object for listing simulations.
  ## @var model_list
  # A biopredyn.ui.tree.TreeElement object for listing models.
  ## @var task_list
  # A biopredyn.ui.tree.TreeElement object for listing tasks.
  ## @var datagen_list
  # A biopredyn.ui.tree.TreeElement object for listing data generators.
  ## @var out_list
  # A biopredyn.ui.tree.TreeElement object for listing outputs.

  ## Overriden constructor.
  # @param self The object pointer.
  # @param parent A biopredyn.ui.navigationtree.NavigationTree object.
  # @param workflow A biopredyn.workflow.WorkFlow object.
  def __init__(self, parent, workflow):
    TreeElement.__init__(self, parent)
    self.workflow = workflow
    self.setText(0, os.path.split(self.workflow.get_source())[1])
    # Build child tree lists
    # list of simulations
    self.sim_list = TreeElement(self)
    self.sim_list.setText(0, 'listOfSimulations')
    self.addChild(self.sim_list)
    for s in workflow.get_simulations():
      self.sim_list.addChild(SimulationElement(s, self.sim_list))
    # list of models
    self.model_list = TreeElement(self)
    self.model_list.setText(0, 'listOfModels')
    self.addChild(self.model_list)
    for m in workflow.get_models():
      self.model_list.addChild(ModelElement(m, self.model_list))
    # list of tasks
    self.task_list = TreeElement(self)
    self.task_list.setText(0, 'listOfTasks')
    self.addChild(self.task_list)
    for t in workflow.get_tasks():
      self.task_list.addChild(TaskElement(t, self.task_list))
    # list of data generators
    self.datagen_list = TreeElement(self)
    self.datagen_list.setText(0, 'listOfDataGenerators')
    self.addChild(self.datagen_list)
    for d in workflow.get_data_generators():
      self.datagen_list.addChild(DataGeneratorElement(d, self.datagen_list))
    # list of outputs
    self.out_list = TreeElement(self)
    self.out_list.setText(0, 'listOfOutputs')
    self.addChild(self.out_list)
    for o in workflow.get_outputs():
      self.out_list.addChild(OutputElement(o, self.out_list))

  ## Overriden. Returns 'self'.
  # @param self The object pointer.
  # @return self
  def get_workflow_element(self):
    return self

  ## Runs the tasks of self.workflow, and processes its outputs.
  # @param self The object pointer.
  def run(self):
    self.workflow.run_tasks()
    self.workflow.process_outputs()

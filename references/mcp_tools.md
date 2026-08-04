# COMSOL MCP Tools Reference

The COMSOL MCP server provides programmatic access to COMSOL Multiphysics. Use these tools alongside mph for results evaluation, image export, and session management.

## Session Management

| Tool | Purpose |
|------|---------|
| `comsol_start` | Start local COMSOL session (cores, version, products) |
| `comsol_connect` | Connect to remote COMSOL server (port, host) |
| `comsol_disconnect` | Disconnect and clear all models |
| `comsol_status` | Get current session status |

## Model Operations

| Tool | Purpose |
|------|---------|
| `model_create` | Create new empty model |
| `model_load` | Load model from .mph file |
| `model_save` | Save model to .mph file |
| `model_clone` | Clone model for comparison |
| `model_remove` | Remove model from memory |
| `model_list` | List all loaded models |
| `model_inspect` | Get detailed model structure |

## Parameters

| Tool | Purpose |
|------|---------|
| `param_set` | Set parameter value (with units) |
| `param_get` | Get parameter value or expression |
| `param_list` | List all parameters |
| `param_sweep_setup` | Configure parametric sweep |

## Geometry

| Tool | Purpose |
|------|---------|
| `geometry_create` | Create geometry sequence |
| `geometry_add_block/circle/cylinder/sphere/rectangle` | Add primitives |
| `geometry_boolean_union/difference` | Boolean operations |
| `geometry_build` | Build geometry sequence |
| `geometry_list/list_features` | List geometries and features |
| `geometry_get_boundaries` | Get boundary info |
| `geometry_create_box_selection` | Create named box selection |
| `geometry_import` | Import CAD file |

## Physics

| Tool | Purpose |
|------|---------|
| `physics_add` | Add generic physics interface |
| `physics_add_electrostatics/solid_mechanics/heat_transfer/laminar_flow` | Add specific interface |
| `physics_add_coefficient_form_pde/general_form_pde/weak_form_pde` | Add PDE interface |
| `physics_configure_boundary` | Set boundary condition |
| `physics_list_features` | List physics features |
| `multiphysics_add` | Add multiphysics coupling |

## Mesh

| Tool | Purpose |
|------|---------|
| `mesh_create` | Create and build mesh |
| `mesh_info` | Get mesh statistics |
| `mesh_list` | List mesh sequences |

## Study & Solve

| Tool | Purpose |
|------|---------|
| `study_create` | Create study (Stationary, TimeDependent, etc.) |
| `study_solve` | Solve study (synchronous) |
| `study_solve_async` | Solve study (background) |
| `study_get_progress` | Get solving progress |
| `study_cancel` | Cancel running solve |
| `study_wait` | Wait for completion |

## Results

| Tool | Purpose |
|------|---------|
| `results_evaluate` | Evaluate expression on dataset |
| `results_global_evaluate` | Evaluate global scalar expression |
| `results_export_image` | Export plot as image |
| `results_export_data` | Export data to file |
| `results_plots_list` | List plot nodes |
| `datasets_list` | List datasets |
| `solutions_list` | List solutions |

## Documentation

| Tool | Purpose |
|------|---------|
| `docs_get` | Get workflow/physics guide |
| `docs_list` | List available docs |
| `pdf_search` | Search COMSOL PDF documentation |
| `pdf_list_modules` | List available documentation modules |

## When to Use MCP vs mph

| Scenario | Use |
|----------|-----|
| Model building (geometry, physics, BCs) | **mph** — more control, full API access |
| Piezo/material matrices | **mph** — MCP cannot set matrix entries |
| Solving | **mph** — more reliable for parameter sweeps |
| Result evaluation (after mph solve fails) | **MCP** — independent COMSOL connection |
| Image export | **MCP** — simpler API |
| Documentation lookup | **MCP** — `pdf_search` is fast |
| Quick parameter check | **MCP** — `param_get/list` work without solve |

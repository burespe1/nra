<!-- Generated from "05 NRA Optional functionality guideline.docx" by tools/docx2md.sh – do not edit, edit the .docx -->

**Purpose:** This guideline defines how optional functionality is documented and represented within the NAP Reference Architecture (NRA). It covers both the **functionality list** and the **Enterprise Architect (EA) model**, ensuring clear differentiation between mandatory and optional elements.

**Audience:** NRA maintenance team.

**Status**: approved on 20 October 2026

| Version | Author             | Note                                                                                                                                          |
| ------- | ------------------ | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 0.9     | Petr Bureš         | First proposal                                                                                                                                |
| 1.0     | Petr Bureš, Claude | Title corrected; RequirementLevel mandatory with derivation rule; colour via diagram legend; template and check. Approved on 20 October 2026. |

# Scope

To support transparency and consistency, optional functionality of the NAP must be explicitly recorded. This requires a visual and structural distinction between mandatory and optional elements in two phases:

  - **Collection phase**: compiling functionality in a list or table.

  - **Modelling phase**: representing functionality in the EA model.

# Introduction

Optional functionality is identified during the initial and review phases. It may range from:

  - Simple actions or tasks that extend required functionality.

  - Complex new features that go beyond the original purpose of the NAP.

This work supports the rethinking of NAP types, distinguishing between **core** and **optional** functionality.

# Documentation Phases

Optional functionality is recorded and differentiated in two products:

## Functionality List

1.  A Word file containing a classified list of functionalities.

2.  Each functionality is broken down into concise processes, each performing a single task.

3.  Mandatory vs. optional is indicated in one of two ways:
    
    1.  **Tabular representation**: a column “Optional” marked with an “X”.
    
    2.  **Linear representation**: separate subheadings for *Mandatory* and *Optional*, each containing the relevant functionalities.
    
    <!-- end list -->
    
    1.  ## EA Model

<!-- end list -->

1.  Functions are represented as objects in the EA functional view of the NAP.

2.  Each function is assigned a tagged value RequirementLevel with one of the following values: The tag is mandatory on every Low Level Function; when the level is not yet decided, MANDATORY is the default.
    
    1.  **MANDATORY** – element contains only mandatory functionality.
    
    2.  **OPTIONAL** – element contains only optional functionality.
    
    3.  **MANDATORY\_PLUS** – element is a mix of mandatory and optional functionality

3.  The level follows the Requirements the function fulfils (see Guideline 03): only MANDATORY requirements → MANDATORY; only OPTIONAL → OPTIONAL; both → MANDATORY\_PLUS. For a function without Requirements the team decides.
    
    1.  Visual differentiation:
        
        1.  Elements with RequirementLevel = OPTIONAL are displayed in a distinct colour. The colour is applied with a diagram legend bound to the tagged value RequirementLevel, so that it follows the tag automatically and is explained on every functional diagram.
    
    2.  In **MANDATORY\_PLUS** elements, optional functionality is clearly delineated by the keyword **OPTIONAL**, followed by the list of optional items.
    
    3.  The documentation template for functions (NC\_NNN\_Functions) prints RequirementLevel next to the function name.

4.  Optional functions may have their own dataflows. These can connect either to the functions they extend (via IN/OUT flows) or to other functions.
    
    1.  ## EA Rules for Creating Optional Functional objects in Model

New optional functionality should be created when:

  - There is a clear delineation between mandatory and optional functionality.

  - Graphical representation is needed to express functionality as optional.

  - Optional functionality introduces new IN and OUT dataflows.

  - New optional functions and new OPTIONAL parts get the tagged value since with the NRA version that introduced them (see Guideline 06).

  - tools/check.py checks that MANDATORY\_PLUS functions contain the keyword OPTIONAL and warns about functions without RequirementLevel.

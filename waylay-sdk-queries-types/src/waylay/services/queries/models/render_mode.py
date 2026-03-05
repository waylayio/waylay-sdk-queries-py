"""Waylay Query: timeseries queries (v1 protocol) models.

This code was generated from the OpenAPI documentation of 'Waylay Query: timeseries queries (v1 protocol)'

Do not edit the class manually.

"""

from __future__ import annotations

from typing import TypeAlias

from ..models.render_compact import RenderCOMPACT
from ..models.render_compactws import RenderCOMPACTWS
from ..models.render_csv import RenderCSV
from ..models.render_flatdict import RenderFLATDICT
from ..models.render_headercolumn import RenderHEADERCOLUMN
from ..models.render_headerrow import RenderHEADERROW
from ..models.render_hierdict import RenderHIERDICT
from ..models.render_metricflatdict import RenderMETRICFLATDICT
from ..models.render_series import RenderSERIES
from ..models.render_upload import RenderUPLOAD

RenderMode: TypeAlias = RenderHEADERROW | RenderCOMPACT | RenderCOMPACTWS | RenderSERIES | RenderHEADERCOLUMN | RenderFLATDICT | RenderHIERDICT | RenderMETRICFLATDICT | RenderUPLOAD | RenderCSV
"""RenderMode."""

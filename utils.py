import unicodedata
from typing import Optional, Set, Dict


def normalize_direction(token: str, direction_map: Dict[str, str], valid_directions: Set[str]) -> Optional[str]:
    """
    Retourne la direction canonique (une des clés de `valid_directions`, p.ex. 'N','S','E','O','U','D')
    ou `None` si le token n'est pas reconnu.

    Normalisation effectuée : suppression des accents + `casefold()` pour être insensible à la casse.

    Args:
        token: la saisie utilisateur à normaliser
        direction_map: table de correspondance (mots -> lettre canonique)
        valid_directions: ensemble des directions valides (ex: {'N','E','S','O','U','D'})

    Returns:
        La lettre canonique ou None si non reconnue.
    """
    if token is None:
        return None

    # Remove accents and normalize
    nfkd = unicodedata.normalize('NFKD', token)
    without_accents = ''.join([c for c in nfkd if not unicodedata.combining(c)])
    key = without_accents.casefold()

    # direct lookup in direction_map (we store multi-letter keys lowercased)
    if key in direction_map:
        return direction_map[key]

    # single-letter directions (N, E, S, O, U, D) may be provided in any case
    up = token.upper()
    if up in valid_directions:
        return up

    return None

# Amapatolli — Referencia del Sistema de Juegos

*Documentación generada a partir de los assets visuales de Estudio Tochcalli.*
*Fuente: iconos e instrucciones proporcionados por Jorge César Rodríguez.*

---

## Visión General

**Amapatolli** es una baraja de la Colección Tonalli de Estudio Tochcalli. No es un solo juego — es un **sistema de juegos** que usa el mismo mazo de cartas (y opcionalmente el tablero Huapalli y fichas/Tetl) para múltiples modos de juego con mecánicas distintas.

### Componentes del sistema
- **Baraja Amapatolli** — cartas con iconografía mesoamericana
- **Tablero Huapalli** — grilla 5×5 con casillas de colores (usado en varios modos)
- **Tetl** (fichas) — piezas de colores para marcar posiciones en tablero

### Anatomía de las cartas
Las cartas tienen dos dimensiones visuales principales:
- **Color de margen** (borde exterior): rojo, azul/cyan, negro, blanco
- **Color de fondo** (interior): puede coincidir o diferir del margen
- **Ilustración central**: iconos de los 20 signos del tonalpohualli (estilo mesoamericano estilizado)
- **Numerales**: puntos (estilo mesoamericano, 1-5+) en la parte superior
- **Cartas especiales**: "Pájaros" (aves) y "Tlapiani" (comodines con ilustración de deidad)

### Paleta de colores
- **Rojo** (tlatlauhqui)
- **Azul/Cyan** (texotli)  
- **Negro** (tliltic)
- **Blanco** (iztac)

Estos cuatro colores corresponden a los 4 rumbos del universo mesoamericano (oriente, norte, poniente, sur) según el Tonalamatl de los Pochtecas.

---

## Iconos del sistema

| Archivo | Descripción | Uso |
|---------|-------------|-----|
| `Jugadores@4x.png` | Dos figuras sentadas frente a frente en mesa | Indicador de número de jugadores |
| `Duracion@4x.png` | Reloj/cronómetro estilo antiguo | Indicador de duración estimada |
| `Edad@4x.png` | Figura adulta y figura menor | Indicador de edad mínima |
| `Tipo@4x.png` | Tres cartas con bombilla, engrane, interrogación | Indicador de tipo de juego (ingenio, estrategia, azar) |
| `Componentes@4x.png` | Tablero cuadriculado + fichas sueltas | Indicador de componentes necesarios |

---

## Modos de Juego (11 documentados)

### 1. CE ("Uno")
- **Tipo:** Cartas, velocidad/descarte
- **Componentes:** Solo baraja
- **Preparación:** Reparte 7 cartas a cada jugador. Baraja el resto, déjalo al centro. Destapa la primera carta.
- **Jugadas — Condiciones de emparejamiento:**
  - Mismo color de margen → juega 1 carta
  - Mismo color de fondo → juega 1 carta
  - Mismos colores (margen Y fondo) → juega 2 cartas
  - Margen y fondo invertidos → juega 2 cartas
  - Pájaros → saltan al siguiente jugador
  - Tlapiani → son comodines (juegan sobre cualquier carta)
- **Objetivo:** Gana el primer jugador en jugar todas las cartas de su mano. ¡Gritar "Ce Amapatolli" cuando solo quede una carta! Si no lo haces, come 3 cartas.
- **Analogía:** Similar a UNO pero con sistema de doble color (margen + fondo)

### 2. IXTLI ("Ojo/Rostro")
- **Tipo:** Tablero + cartas, observación/velocidad
- **Componentes:** Baraja + tableros Huapalli (1 por jugador) + fichas Tetl
- **Preparación:** Reparte un tablero y 7 fichas a cada jugador. Coloca el mazo al centro. Otorga el mazo al cantor de cartas.
- **Jugadas:** El cantor destapa una carta. Los jugadores buscan la ilustración en su tablero. Gritar "Ixtli" al encontrarlo. El primer jugador en encontrarlo coloca su ficha.
- **Objetivo:** El primero en colocar 7 fichas en su tablero gana.
- **Analogía:** Lotería mexicana con mecánica de velocidad

### 3. PAMITL ("Bandera/Fila")
- **Tipo:** Tablero + fichas, estrategia abstracta
- **Componentes:** Tablero Huapalli + fichas Tetl
- **Objetivo:** 5 fichas en fila, en cualquier dirección, hacen un Pamitl. Gana quien lo logre primero.
- **Analogía:** Similar a Conecta 4/Gobang en tablero mesoamericano

### 4. PINOTL ("Pila/Montón")
- **Tipo:** Cartas, emparejamiento
- **Componentes:** Solo baraja
- **Objetivo:** Gana el primer jugador en terminar con todas las cartas de su mano una vez que se ha terminado el mazo.

### 5. TECUIA ("Golpear")
- **Tipo:** Cartas, secuencia/posicionamiento
- **Componentes:** Solo baraja (cartas con numerales)
- **Objetivo:** Gana colocando 5 cartas consecutivas de tu color en cualquier dirección.
- **Nota:** Las cartas tienen puntos (numerales mesoamericanos) que determinan el orden

### 6. ATOYATL ("Río")
- **Tipo:** Cartas, descarte por valor
- **Componentes:** Solo baraja (cartas numeradas)
- **Objetivo:** Gana el primer jugador en colocar la última de sus cartas boca abajo. Las cartas muestran valores numéricos (ej: 18, 10) que determinan las jugadas válidas.

### 7. CAYAHUA ("Dejar caer/Esparcir")
- **Tipo:** Tablero + fichas, estrategia abstracta
- **Componentes:** Tablero Huapalli + fichas Tetl (colores azul oscuro)
- **Jugadores:** 2
- **Objetivo:** Gana el jugador que deja a su rival sin ningún Tetl. 
- **Nota:** Tablero en formación de diamante con fichas

### 8. TLALPOLOA ("Devorar la tierra")
- **Tipo:** Tablero + fichas, colocación
- **Componentes:** Tablero Huapalli + fichas Tetl (colores cyan)
- **Objetivo:** Coloca todas tus fichas en el tablero (formación de diamante).

### 9. CEMPOHUALLI ("Veinte")
- **Tipo:** Cartas, supervivencia
- **Componentes:** Solo baraja
- **Objetivo:** Cada carta es una vida. Al perder tus tres cartas pierdes el juego. ¡El último jugador en pie es el ganador!
- **Analogía:** Juego de eliminación

### 10. PALEHUIA ("Ayudar")
- **Tipo:** Cartas, cooperativo
- **Componentes:** Baraja + fichas Tetl
- **Objetivo:** Completar 4 pilas (1 por color) del 1 al 5. Cuando una pila llega al 5, se retira del centro.
- **Condiciones de derrota:**
  - Se queman 3 pilas (máximo 6 pilas al centro)
  - Se agotan los Tetl del color necesario
  - El mazo se agota antes de completar 4 pilas
- **Nota:** Es el único modo cooperativo documentado

### 11. TLAPATLANI ("Intercambiar")
- **Tipo:** Cartas, colección por categorías
- **Componentes:** Solo baraja
- **Objetivo:** Gana quien complete primero sus 4 pilas (colecciones organizadas por tipo de ilustración: aves, templos, árboles, figuras).

---

## Elementos clave del sistema de diseño

### Propiedades de emparejamiento (fundamentales)
El sistema Amapatolli se basa en **emparejamiento por múltiples atributos**:
1. Color de margen
2. Color de fondo
3. Ilustración (signo del tonalpohualli)
4. Valor numérico (puntos)
5. Tipo/categoría de ilustración

Cada juego usa un subconjunto diferente de estos atributos como mecánica principal.

### Cartas especiales
- **Tlapiani** (comodines): cartas con ilustración de deidad. Funcionan como comodines en modos de emparejamiento.
- **Pájaros**: cartas con ilustración de ave. Efecto especial de "saltar turno" o acción sobre siguiente jugador.

### Componentes modulares
| Componente | Juegos que lo usan |
|------------|-------------------|
| Solo baraja | Ce, Pinotl, Tecuia, Atoyatl, Cempohualli, Tlapatlani |
| Baraja + tablero + fichas | Ixtli, Palehuia |
| Solo tablero + fichas | Pamitl, Cayahua, Tlalpoloa |

---

## Estructura de archivos

```
proyectos/amapatolli/
├── assets/          # (pendiente: assets generales, renders)
├── docs/
│   └── AMAPATOLLI-REFERENCIA.md  ← este archivo
├── iconos/          # Iconos de metadata de juego
│   ├── Componentes@4x.png
│   ├── Duracion@4x.png
│   ├── Edad@4x.png
│   ├── Jugadores@4x.png
│   └── Tipo@4x.png
└── instrucciones/   # Guías visuales por juego (3 imágenes c/u)
    ├── Preparación [Juego]@4x.png  — setup inicial
    ├── Jugadas [Juego]@4x.png      — cómo jugar
    └── Objetivo [Juego]@4x.png     — condición de victoria
```

Cada juego tiene hasta 3 imágenes: Preparación, Jugadas, Objetivo.

---

## Notas para la expansión Yohualli

La propuesta de palo nocturno (21 cartas: 7 Señores + 7 Encrucijadas + 7 Ofrendas) debe considerar:

1. **Compatibilidad con emparejamiento dual**: las nuevas cartas necesitan margen + fondo para funcionar en Ce
2. **Numerales**: si llevan valor, funcionan también en Tecuia y Atoyatl
3. **Categoría visual**: si las ilustraciones son reconocibles, funcionan en Ixtli y Tlapatlani
4. **Fichas**: si se agregan fichas de un 5to color (ej: púrpura/morado para "noche"), funcionan en Pamitl, Cayahua, Tlalpoloa
5. **Efectos especiales**: las Tlapiani ya son comodines y los Pájaros saltan turno. Las nuevas cartas podrían traer efectos adicionales (invertir dirección, robar carta, etc.) sin romper los modos existentes

### Las 4 Tlapiani (comodines) actuales
Cada una asociada a un color de la baraja:

| Deidad | Náhuatl | Color | Dominio |
|--------|---------|-------|---------|
| Itztli | "Cuchillo de Pedernal" | Blanco (iztac) | Sacrificio, justicia |
| Tláloc | "Dios de la lluvia" | Negro (tliltic) | Lluvia, fertilidad, agua celeste |
| Tlazoltéotl | "Diosa de las inmundicias" | Rojo (tlatlauhqui) | Purificación, placer, confesión |
| Mictlantecuhtli | "Dios de la muerte" | Azul (texotli) | Muerte, inframundo, tránsito |

Estos 4 son parte de los 9 Señores de la Noche (Yohualteteuctin). Los 5 restantes para la expansión Yohualli:

| # | Deidad | Náhuatl | Dominio | Fuente (Tonalamatl) |
|---|--------|---------|---------|---------------------|
| 5 | Xiuhtecuhtli | "Señor del fuego" | Fuego, centro cósmico, transformación | Pág 1 (centro), Pág 2 |
| 6 | Tonatiuh-Piltzintecuhtli | "Sol joven" | Sol, luz, ciclos, tiempo | Pág 2 |
| 7 | Chalchiuhtlicue | "La de la falda de jade" | Agua terrestre, jade, fertilidad | Pág 3 |
| 8 | Cintéotl | "Dios del maíz" | Sustento, crecimiento, maíz | Pág 3 |
| 9 | Tepeyóllotl | "Corazón del monte" | Eco, cavernas, jaguar, interior de la tierra | Pág 4 |

---

*Generado: 2026-03-17 | Fuente: assets visuales de Estudio Tochcalli*
*Pendiente: imágenes de cartas individuales, reglas completas en texto, assets del tablero Huapalli*

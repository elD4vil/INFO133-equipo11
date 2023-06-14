CREATE TABLE Pais (
  ID_Pais INT PRIMARY KEY,
  Nombre_Pais VARCHAR(20)
);

CREATE TABLE Region (
  ID_Region INT PRIMARY KEY,
  Nombre_Region VARCHAR(20),
  ID_Pais INT,
  FOREIGN KEY (ID_Pais) REFERENCES Pais(ID_Pais)
);

CREATE TABLE Comuna (
  ID_Comuna INT PRIMARY KEY,
  Nombre_Comuna VARCHAR(20),
  Poblacion INT,
  Densidad FLOAT,
  Superficie INT,
  Longitud VARCHAR(20),
  Latitud VARCHAR(20),
  ID_Region INT,
  FOREIGN KEY (ID_Region) REFERENCES Region(ID_Region)
);

CREATE TABLE Indicador (
  Nombre_Indicador VARCHAR(20) PRIMARY KEY,
  Categoria VARCHAR(20),
  Descripcion VARCHAR(255)
);

CREATE TABLE Torre (
  ID_Torre INT PRIMARY KEY,
  Direccion VARCHAR(20),
  Empresa VARCHAR(20),
  Fecha_Ingreso DATE,
  Long_Torre VARCHAR(20),
  Lat_Torre VARCHAR(20),
  ID_Comuna INT,
  FOREIGN KEY (ID_Comuna) REFERENCES Comuna(ID_Comuna)
);

CREATE TABLE Delito (
  Tipo_Info VARCHAR(20),
  Periodo DATE,
  Tipo_Delito VARCHAR(20),
  Umbral FLOAT,
  ID_Comuna INT,
  PRIMARY KEY (Tipo_Info, Periodo),
  FOREIGN KEY (ID_Comuna) REFERENCES Comuna(ID_Comuna)
);

CREATE TABLE PanoramaLaboral (
  Sexo VARCHAR(1),
  Rango_Edad VARCHAR(20),
  Nvl_Educacion VARCHAR(20),
  Ingreso_Medio FLOAT,
  Personas_Ocupadas INT,
  Personas_Desocupadas INT,
  Tasa_Desempleo FLOAT,
  ID_Comuna INT,
  PRIMARY KEY (Sexo, Rango_Edad, Nvl_Educacion),
  FOREIGN KEY (ID_Comuna) REFERENCES Comuna(ID_Comuna)
);

CREATE TABLE EstablecimientoSalud (
  Nombre_Establecimiento VARCHAR(255) PRIMARY KEY,
  Privado BOOLEAN,
  Direccion VARCHAR(20),
  Telefono INT,
  ID_Comuna INT,
  FOREIGN KEY (ID_Comuna) REFERENCES Comuna(ID_Comuna)
);

CREATE TABLE poseer (
  ID_Comuna INT,
  Nombre_Indicador VARCHAR(20),
  Año INT,
  Valor FLOAT,
  PRIMARY KEY (ID_Comuna, Nombre_Indicador),
  FOREIGN KEY (ID_Comuna) REFERENCES Comuna(ID_Comuna),
  FOREIGN KEY (Nombre_Indicador) REFERENCES Indicador(Nombre_Indicador)
);

#encoding: UTF-8
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS
import os

DWC = Namespace('http://rs.tdwg.org/dwc/terms/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')


coleccion = Namespace('http://sparql.databio.com.co/databio/')

g = Graph()

g.add( (URIRef(coleccion['descripcion.rdf']), skos.related, coleccion['HerbarioTULV.rdf']) )

g.add( (URIRef(coleccion['descripcion.rdf']), RDFS.label, Literal("HERBARIO TULV INCIVA", lang='es')) )
g.add( (URIRef(coleccion['descripcion.rdf']), RDFS.comment, Literal("""Es una coleccion biologica que comprenden los especimenes vegetales que se albergan en el Jardin Botanico Juan Maria Cespedes en el municipio de Tulua, Valle del Cauca""", lang='es')))

g.bind("dwc", DWC)

rdf = g.serialize(destination='descripcion.rdf', format='xml')

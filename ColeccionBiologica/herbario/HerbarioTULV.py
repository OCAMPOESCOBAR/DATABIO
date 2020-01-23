#encoding: UTF-8
import sys
from os import path
sys.path.append( path.dirname( path.dirname( path.abspath(__file__) ) ) )

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, RDFS

OWL = Namespace('http://www.w3.org/2002/07/owl#')

DWC = Namespace('http://rs.tdwg.org/dwc/terms/')
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
UMBEL = Namespace('http://umbel.org/umbel#')


coleccion = Namespace('https://190.24.5.78/databio/ColeccionBiologica/')
herbario = Namespace('https://190.24.5.78/databio/ColeccionBiologica/HerbarioTULV/')

uniprot = Namespace('http://www.uniprot.org/taxonomy/')

g = Graph()

def especimen(uri, recorded_By, scientific_Name, family, institution_Code, continent, country, state_Province, county, municipality, locality, uriLink1):
	g.add( (URIRef(uri), DWC.recordedBy, Literal(recorded_By) ) )
	g.add( (URIRef(uri), DWC.scientificName, Literal(scientific_Name)) )
	g.add( (URIRef(uri), DWC.family, Literal(family)) )
	g.add( (URIRef(uri), DWC.institutionCode, Literal(institution_Code)))
	g.add( (URIRef(uri), DWC.continent, Literal(continent)) )
	g.add( (URIRef(uri), DWC.country, URIRef(country)) )
	g.add( (URIRef(uri), DWC.stateProvince, URIRef(state_Province)) )
	g.add( (URIRef(uri), DWC.county, URIRef(county)) )
	g.add( (URIRef(uri), DWC.municipality, URIRef(municipality)) )
	g.add( (URIRef(uri), DWC.locality, URIRef(municipality)) )

	g.add( (URIRef(uri), OWL.sameAs, URIRef(uriLink1)) ) #Link RDF
	
	
	g.add( ( URIRef(uri), UMBEL.isAbout, URIRef(coleccion['herbario.rdf'])) )

especimen(
	coleccion['Herbario.rdf#Achatocarpus'],
	"A. Castaño N, W. Devia",
	"Achatocarpus nigricans Triana",
	"ACHATOCARPACEAE",
	"Instituto para la Investigación y la Preservación del Patrimonio Cultural y Natural del Valle del Cauca",
	"SA",
	"Colombia",
	"Valle del Cauca",
	"Obando",
	"San Isidro",
	"Obando Via San Isidro, finca Cristales",
	uniprot['1904701']
)

g.bind("dwc", DWC)

print("--- Grafo ---")
print( g.serialize(format='xml') )
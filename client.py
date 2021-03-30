#!/usr/bin/env python3

# ============================= Torrent - Client =============================
# Sistema torrent para Redes de Computadores
# UFMG - 2020/2
# Desenvolvido por Jonas Ferreira da Trindade
# Março de 2021
# ============================================================================

import sys
import socket
import struct

def main():

  if len(sys.argv) != 4:
    print("favor passar ip, porto e chunks (ip port 2,3,4)")
    return

  peer_access_address = sys.argv[1]
  peer_access_port = sys.argv[2]
  chunks = sys.argv[3]
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  print(peer_access_address)
  print(peer_access_port)
  print(chunks)

if __name__ == "__main__":
    print(sys.version)
    main()

def atribuir_chunks():
  # ler chunks
  # armazenar no struct client os chunks
  # que ele deseja fazer download
  return true

def concetar_ao_peer_acesso():
  # fazer conexao com o peer usando
  # access_peer_address e access_peer_port

def disparar_hello():
  # enviar mensagem udp
  # HELLO 1
  # [n_chunks: 2 bytes]
  # [chunks_ids: 2 bytes]
  # CHUNKS_INFO 3
  # receber response
  # [n_chunks: 2 bytes]
  # [chunks_ids: n_chunks * 2 bytes]
  # acumular peers com chunks 
  # desejados
  # guardar files output-IP.log
  # na pasta Outputs
  return true


def escolher_random_chunk(chunks):
  # escolher randomicamente caso
  # mais de um peer tiver o mesmo 
  # chunk desejado
  return true





#  list blob and metdata
from azure.storage.blob import ContainerClient, __version__
from azure.storage.blob import BlobServiceClient, BlobClient

connect_str = "BlobEndpoint=https://minkonto.blob.core.windows.net/;QueueEndpoint=https://minkonto.queue.core.windows.net/;FileEndpoint=https://minkonto.file.core.windows.net/;TableEndpoint=https://minkonto.table.core.windows.net/;SharedAccessSignature=sv=2021-12-02&ss=bfqt&srt=sco&sp=rwdlacupiytfx&se=2023-06-30T13:41:12Z&st=2023-05-03T05:41:12Z&spr=https&sig=YRtN%2FYiPlnSv4HGaxiVMcnoHUepI4lcLt4i8KkCfG6w%3D"
container_name = "photos" 
blob_service_client = BlobServiceClient.from_connection_string(conn_str=connect_str) # create a blob service client to interact with the storage account
container_client = blob_service_client.get_container_client(container=container_name) # get container client to interact with the container in which images will be stored
container = ContainerClient.from_connection_string(conn_str=connect_str, container_name=container_name)

bildefil = []

blobs = container_client.list_blobs(include=["metadata"])
for i in blobs:
    if i["metadata"] is not None:
        bildefil.append(i.name)
        print(i.metadata)
        print(i.name)
    blob_client = container_client.get_blob_client(blob=i.name)
    blob_url = blob_client.url
    print(blob_url)    

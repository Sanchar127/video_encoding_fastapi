import clamd
import io

def scan_file_stream(file_stream: io.BytesIO):
    try:
        cd = clamd.ClamdNetworkSocket()  # Connects to localhost:3310 
        result = cd.instream(file_stream)

        if not result:
            return {"status": "clean"}

        status, virus = result.get('stream', ('OK', None))
        if status == 'FOUND':
            return {"status": "infected", "virus": virus}
        else:
            return {"status": status}
    except Exception as e:
        return {"status": "error", "message": str(e)}

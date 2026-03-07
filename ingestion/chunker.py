def is_valid_chunk(text):

    if len(text.split()) < 40:
        return False

    if "plt." in text or "import " in text:
        return False

    if "www." in text or "email:" in text:
        return False

    return True


def chunk_text(text, max_words=250):

    paragraphs = text.split("\n")

    chunks = []
    current_chunk = []
    current_length = 0

    for para in paragraphs:

        words = para.split()

        if len(words) == 0:
            continue

        if current_length + len(words) <= max_words:

            current_chunk.append(para)
            current_length += len(words)

        else:

            chunk = " ".join(current_chunk)

            if is_valid_chunk(chunk):
                chunks.append(chunk)

            current_chunk = [para]
            current_length = len(words)

    if current_chunk:

        chunk = " ".join(current_chunk)

        if is_valid_chunk(chunk):
            chunks.append(chunk)

    return chunks
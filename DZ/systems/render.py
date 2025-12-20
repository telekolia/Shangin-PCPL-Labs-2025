class RenderSystem():
    def draw(self, entities, TextureManager, window):
        entities_to_draw = []
        for entity in entities:
            if 'Renderable' in entity and 'Position' in entity:
                entities_to_draw.append(entity)

        entities_to_draw.sort(key=lambda e: e['Renderable'].layer)

        for entity in entities_to_draw:
            pos = entity['Position']
            renderable = entity['Renderable']

            window.blit(TextureManager.get(renderable.texture_name), (pos.x * 64, pos.y * 64))

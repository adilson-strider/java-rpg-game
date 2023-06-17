var customMapFormat = {
    name: "Arquivo de texto",
    extension: "txt",

    write: function(map, fileName) {
        var content = "";

        for (var i = 0; i < map.layerCount; ++i) {
            var layer = map.layerAt(i);
            if (layer.isTileLayer) {
                for (var y = 0; y < layer.height; ++y) {
                    var row = "";
                    for (var x = 0; x < layer.width; ++x) {
                        var tileId = layer.cellAt(x, y).tileId;
                        row += tileId + " ";
                    }
                    row = row.trim(); // Remove espaços em branco extras no final da linha
                    content += row + "\n";
                }
            }
        }

        content = content.trim(); // Remove espaços em branco extras no final do conteúdo

        var file = new TextFile(fileName, TextFile.WriteOnly);
        file.write(content);
        file.commit();
    },
};

tiled.registerMapFormat("txt", customMapFormat);
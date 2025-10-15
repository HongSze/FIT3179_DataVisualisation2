const specs = {
  map:    "Charts/global_pollution_map.vg.json",
  gas:    "Charts/monthly_pollutant_line_chart.vg.json",
  ghg:    "Charts/ghg_stacked_area_chart.vg.json",
  global: "Charts/malaysia_api_bar_chart.vg.json",
  range:  "Charts/min_max_range_graph.vg.json"
};

const opts = { actions: false };

Promise.all([
  vegaEmbed("#map",    specs.map,    opts),
  vegaEmbed("#gas",    specs.gas,    opts),
  vegaEmbed("#ghg",    specs.ghg,    opts),
  vegaEmbed("#global", specs.global, opts),
  vegaEmbed("#minmax", specs.range,  opts)
]).catch(console.error);
